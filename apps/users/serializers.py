from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
from datetime import datetime, timedelta

from rest_framework.validators import UniqueValidator

from .models import VerifyCode

from Shop.settings import REGEX_MOBILE

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile):
            raise serializers.ValidationError("距离上次发送验证码不到一分钟")

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, label="验证码", max_length=4, min_length=4, write_only=True,
                                 error_messages={
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误",
                                     "blank": "请输入验证码"

                                 }, help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def create(self, validated_data):
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("add_time")
        if verify_records:
            last_records = verify_records[len(verify_records)-1]
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minutes_ago > last_records.add_time:
                raise serializers.ValidationError("验证码过期")
            if str(last_records) != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")
