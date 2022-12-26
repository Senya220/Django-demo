from django import forms
from django.forms import fields


#limit length of input
class Auth(forms.Form):
    username = fields.CharField(
        max_length=18,
        min_length=4,
        label='username'
    )

    password = fields.CharField(
        widget=forms.PasswordInput(),
        min_length=10,
        label='password'
    )

    #global verify Second
    def clean(self):
        username = self.cleaned_data.get('username','')
        password = self.cleaned_data.get('password','')
        if not username:
            raise forms.ValidationError('username should not be empty')
        if len(username) > 10:
            raise forms.ValidationError('username length should not great than 10')
        if not password:
            raise forms.ValidationError('password should not be empty')

    # #single verrify  First
    # def clean_username(self):
    #     username = self.cleaned_data.get('username', '')
    #     if len(username) > 10:
    #         raise forms.ValidationError("username length can't exceed 5 characters")
    #     return username




# class AuthModelForm(forms.ModelForm):
#     class Meta:
#         #bind model
#         model = Auth
#
#         #渲染我们想要展示的模型字段
#         fields = ['username','password']
#
#         #
#         '''
#         如果大家想要渲染出所有的模型字段:
#         fields = '__all__'
#
#         定义不想渲染的字段:
#         exclude = ['fake']
#         '''
#
#         #定义字段类型，一般情况使用默认的转换类型，很少用
#         field_classes = {
#             'username': forms.CharField,
#             'password': forms.CharField
#         }
#
#
#         #设置label中文名称
#         labels = {
#             'username': '用户名',
#             'password': '密码'
#         }
#
#         #设置表单输入框显示的字符
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={'placeholder':'please input 用户名'}
#             ),
#             'password': forms.PasswordInput(
#                 attrs={'placeholder': 'please input 密码'}
#             )
#         }
#
#         #error msg promote
#         error_message = {
#             'username': {'required':'error_msg: username should not be empty'},
#             'password': {'min_legth': 'error_msg: should not be empty'},
#
#         }
#
#         #single filter
#         def clean_username(self):
#             pass




























