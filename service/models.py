from django.db import models

# Create your models here.
CATEGORY = [
    ('1','Пластическая хирургия'),
    ('2','Флебология'),
    ('3','Травматология и ортопедия'),
]

class Service(models.Model):
    
    title = models.CharField('название услуги', max_length=100)
    slug = models.SlugField('путь', max_length=100)
    description = models.TextField('описание', blank=True, null=True)
    advantage = models.TextField('приемущества', blank=True, null=True)
    image = models.ImageField('фото', upload_to='service_image/')
    category = models.CharField('категория',choices=CATEGORY, max_length=40 )
    

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        """Return absolute url for Service."""
        return ('')
    
class Parametr(models.Model):
    title = models.CharField('название', max_length=100)
    description = models.CharField('информация', max_length=150, blank=True, null=True)
    service = models.ForeignKey(Service, models.CASCADE, related_name='parametr_service')
    
    def __str__(self):
        return 'Параметр'
    
    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

class Benefit(models.Model):
    service = models.ForeignKey(Service, models.CASCADE, related_name='benefit_service')
    title = models.CharField('описание', max_length=55)
    
    def __str__(self):
        return 'Плюсы'
    
    class Meta:
        verbose_name = 'Плюс'
        verbose_name_plural = 'Плюсы'
    
    
class Question(models.Model):
    question = models.CharField('вопрос', max_length=100)
    answer = models.CharField('ответ', max_length=100)
    service = models.ForeignKey(Service, models.CASCADE, related_name='question_service')

    def __str__(self):
        return 'Вопросы'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
class BeforeAfter(models.Model):
    image = models.ImageField('фото', upload_to='befor_after/')
    service = models.ForeignKey(Service, models.CASCADE, related_name='image_af_bef_service')

    def __str__(self):
        return 'Фото До и После'

    class Meta:
        verbose_name = 'Фото До и После'
        verbose_name_plural = 'Фото До и После'
    
class Team(models.Model):
    
    name = models.CharField('имя', max_length=50)
    experience = models.SmallIntegerField('стаж')
    image = models.ImageField('фото', upload_to='team/')
    
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Учасник'
        verbose_name_plural = 'Команда'
        
class Feedback(models.Model):
    
    name = models.CharField('имя', max_length=50)
    text = models.TextField('отзыв', blank=True, null=True)
    phone = models.CharField('номер телефона', max_length=50)
    date = models.DateField('дата', auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        
class RequestOfLeave(models.Model):
    phone = models.CharField('номер телефона', max_length=50)
     
    def __str__(self):
        return f'Заявка номер {self.pk}'
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        
class Appointment(models.Model):
    name = models.CharField('имя', max_length=50)
    email = models.EmailField('почта')
    phone = models.CharField('номер телефона', max_length=50)
     
    def __str__(self):
        return f'Запись на прием  {self.name} к {self.doctor.name}'
    
    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'
        
        
class Setting(models.Model):
    
    phone = models.CharField('номер телефона', max_length=50)
    email = models.EmailField('почта')
    operating_mode = models.CharField('режим работы', max_length=50)
    address = models.CharField('адрес',max_length=100)
    fecebook = models.URLField('фейсбук')
    instagram = models.URLField('инстаграм')
    whatsapp = models.URLField('ватсап')
    
    
    def __str__(self):
        return f'Настройка сайта'
    
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'
        
class Sale(models.Model):
    
    title = models.CharField('описание', max_length=150)
    image = models.ImageField('фото', upload_to='sale_image/')
    description = models.CharField('информация', max_length=150, blank=True, null=True)
    price = models.SmallIntegerField('цена')
    first_price = models.SmallIntegerField('первоначальная цена')

    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'