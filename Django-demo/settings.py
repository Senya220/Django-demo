"""
Django settings for Django-demo project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#返回项目的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#数据加密 防止网站被跨域攻击
SECRET_KEY = '5j7-jpwi2x_j+4^+j7eq*0kqr7$n)bbdhk7pu-ss0!!ozmh_ld'

# SECURITY WARNING: don't run with debug turned on in production!
#网站处于开发模式,开发完成后  一定要改成false
DEBUG = True
#网站访问白名单 ip地址  [‘*’]  通配符 允许任何网站访问
# ALLOWED_HOSTS = ['10.4.4.190','10.4.13.213','127.0.0.1']
ALLOWED_HOSTS = ['*']

# Application definition
#应用注册
INSTALLED_APPS = [
    #定要注释该应用及其url路由，否则会报错： (admin.E403)（红色） A’django.template.backends.django.DjangoTemplates’ instance must be configured in TEMPLATES in order to use the admin application
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
#中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#网站入口 根据路由配置
ROOT_URLCONF = 'Django-demo.urls'
#配置html静态文件
TEMPLATES = [
    {
        # jinja2 template config
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # 获取app jinja2中templates模板html文件地址
        'DIRS': [os.path.join(BASE_DIR, "jinja_templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'environment': 'app.base_jinja2.environment'
        },
    },
    {
        #django default template
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #if templates folder inside app,then replace "templates" with "app.templates"
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#配置开发服务器
WSGI_APPLICATION = 'Django-demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#配置数据库
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',# db name, you have to create before use
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '', #default 127.0.0.1
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
#配置用户密码加密
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
#网站默认语言 en-us
LANGUAGE_CODE = 'zh-hans'
#默认时间 Asia/Shanghai
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
#
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


#static folder  images
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]