from django.db import models
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator

# Create your models here.
class Course(models.Model):
	title 			= models.CharField(max_length = 450, default='Default title !!!')
	image 			= models.ImageField(blank=True, null=True, default = 'CourseDefault.jpg',upload_to = 'Course/%Y/%m/%d/',verbose_name="Main Image")
	image1 			= models.ImageField(blank=True, null=True, upload_to = 'Course/%Y/%m/%d/',verbose_name="2nd Image")
	image2 			= models.ImageField(blank=True, null=True, upload_to = 'Course/%Y/%m/%d/',verbose_name="3rd Image")
	image3 			= models.ImageField(blank=True, null=True, upload_to = 'Course/%Y/%m/%d/',verbose_name="4th Image")
 
	price 			= models.DecimalField(decimal_places=2, max_digits=20, default=0,verbose_name="Course Price",validators=[MinValueValidator(0.0)])
	discount_price  = models.DecimalField(blank=True,null=True,decimal_places=2, max_digits=20, verbose_name="Discount Price",validators=[MinValueValidator(0.0)]) 
	slug 			= models.SlugField(blank=True,unique=True)
	description 	= RichTextField()
	additional_info = RichTextField(blank=True,null=True)
	# category		= models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	# label			= models.CharField(choices=LABEL_CHOICES, max_length=1)
		
 
	featured		= models.BooleanField(default=False, verbose_name="Featured Course")
	created			= models.DateTimeField(auto_now_add=True)
	modified 		= models.DateTimeField(auto_now=True)
	history			= HistoricalRecords()
	
	class Meta:
		ordering = ['-created']
		verbose_name_plural = 'Courses'
	
	def __str__(self):
		return self.title

	def __unicode__(self):
	    return self.title
	# def get_absolute_url(self):
	# 	return reverse("core:product",kwargs={'slug':self.slug})

	# def add_to_cart_url(self, path):
	# 	return reverse("core:add_to_cart",kwargs={'slug':self.slug,'redslug':path},)
    
	# def remove_from_cart_url(self,):
    # 		return reverse("core:remove_from_cart",kwargs={'slug':self.slug})

	# def cart_delete_url(self):
	# 	return reverse("core:delete_from_cart",kwargs={'slug':self.slug})