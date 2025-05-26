import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

class EntryForm(AbstractBaseUser,PermissionsMixin):
    #アカウント情報
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_active = models.BooleanField(_('active'),default=True)
    is_admin = models.BooleanField(_('admin status'),default=True)
    #出欠
    attendance = models.BooleanField(_("出欠"),default=True)

    #名前
    nameFamily = models.CharField(_("名字"), max_length=10,default="")
    nameFirst = models.CharField(_("名前"), max_length=10,default="")
    nameHFamily = models.CharField(_("名字(ひらがな)"), max_length=10,default="")
    nameHFirst = models.CharField(_("名前(ひらがな)"), max_length=10,default="")

    #電話番号
    telNumberRegex = RegexValidator(regex=r'^[0-9]+$', message = ("電話番号は次のように入力してください。: '09012345678' ※半角英数字、最大15桁"))
    telNumber = models.CharField(_('電話番号'), unique=True,validators=[telNumberRegex], max_length=15,default="")

    #メールアドレス
    email = models.EmailField(_("メールアドレス"),unique=True,default="")
    #住所
    #郵便番号
    postalCodeRegex = RegexValidator(regex=r'^[0-9]+$', message = ("郵便番号は次のように入力してください。: '1234567' ※半角英数字、最大7桁"))
    postalCode = models.CharField(_('郵便番号'),validators=[postalCodeRegex], max_length=7,default="")
    #都道府県の選択肢をchoicesオプションにてセット
    prefecture  = models.CharField(_("都道府県"),choices=settings.PREFECTURES,max_length=4,default="岡山県")
    #市区町村
    city = models.CharField(_("市区町村"),max_length=50, default="")
    #番地
    streetAddress = models.CharField(_("番地"),max_length=50, default="")
    #建物名・号室
    building = models.CharField(_("建物名・号室"),max_length=50,blank=True,null=True)

    #アレルギー等
    allergy = models.TextField(_("アレルギー等"),blank=True,null=True)

    #送迎バス
    bus = models.BooleanField(_("送迎バス"),default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'EntryForm'
        verbose_name = _('user')
        verbose_name_plural = _('ユーザー')
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    def get_name(self):
        name = '%s %s' % (self.nameFamily,self.nameFirst)
        return name.strip()
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
    # def __str__(self):
    #     return self.nameFamily + self.nameFirst

class FavoriteModel(models.Model):
    name = models.CharField(verbose_name="バンド名",max_length=50,default="")
    imageURL = models.URLField(verbose_name="画像リンク")
    iconURL = models.URLField(verbose_name="アイコンリンク")
    twitterURL = models.URLField(verbose_name="ツイッターリンク",blank=True,null=True)
    youtubeURL = models.URLField(verbose_name="YouTubeリンク",blank=True,null=True)
    applemusicURL = models.URLField(verbose_name="AppleMusicリンク",blank=True,null=True)
    spotifyURL = models.URLField(verbose_name="Spotifyリンク",blank=True,null=True)

    def __str__(self):
        return self.name

class GalleryModel(models.Model):
    image = models.ImageField(verbose_name="ギャラリー",upload_to='photo/')