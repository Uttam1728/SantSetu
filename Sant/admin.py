from django.contrib import admin

# Register your models here.
from django.db.models import ImageField
from client_side_image_cropping import ClientsideCroppingWidget
from django.utils.html import format_html
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import DikshaDetails, AnuvrutiDetails, Attachments, PurvashramDetails, Sant


class DikshaDetailsInline(admin.StackedInline):
    model = DikshaDetails
    extra = 0
    classes = ['collapse']
    max_num = 3


class AnuvrutiDetailsInline(admin.StackedInline):
    model = AnuvrutiDetails
    extra = 0
    classes = ['collapse']


class PurvashramDetailsInline(admin.StackedInline):
    model = PurvashramDetails
    extra = 0
    classes = ['collapse']


class AttachmentsInline(admin.StackedInline):
    model = Attachments
    extra = 0
    formfield_overrides = {
        ImageField: {'widget': ClientsideCroppingWidget(
            width=500,
            height=300,
            preview_width=250,
            preview_height=150,
        ), },
    }
    classes = ['collapse']

class AttachmentsReadInline(admin.StackedInline):
    model = Attachments
    extra = 0
    formfield_overrides = {
        ImageField: {'widget': ClientsideCroppingWidget(
            width=500,
            height=300,
            preview_width=250,
            preview_height=150,
        ), },
    }
    classes = ['collapse']
    readonly_fields = ('photolink', 'discripttion')


class SantAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ImageField: {'widget': ClientsideCroppingWidget(
            width=300,
            height=300,
            preview_width=150,
            preview_height=150,
        ), },
    }
    list_display = ('__str__', 'santimage', 'WhatsApp', 'Call', 'SMS', 'remark')
    inlines = (PurvashramDetailsInline, DikshaDetailsInline, AnuvrutiDetailsInline, AttachmentsInline)
    # list_filter = ('Name', 'mobile_no')
    search_fields = ('Name', 'mobile_no', 'english_name')
    fieldsets = ()
    list_display_links = ('__str__',)
    fieldsets = (("Profile", {"fields": ["Photo", "Name", "english_name", "mobile_no", 'remark' ],
                              }),
                 )

    def santimage(self, obj):
        if obj.Photo:
            s = '<img src={} height="100px" width="100px" style="border-radius: 50%;border: 1px solid black" alt="profilepic"/></div>'.format(
                obj.Photo.url)
        else:
            s = '<img  height="80px" width="80px" src="/static/img/yuvak.png" >'
        return format_html(s)

    santimage.short_description = " "

    def WhatsApp(self, obj):
        buttons = ''
        buttons += "<a href='https://wa.me/+91{}' target='_blank'><i class='fa fa-whatsapp' style='font-size:30px;color:green'></i></a>".format(
            obj.mobile_no)
        return format_html(buttons)

    WhatsApp.short_description = " "

    def Call(self, obj):
        buttons = ''
        buttons += "<a href='tel:+91{}' target='_blank'> <i class='fa fa-volume-control-phone' style='font-size:27px;color:deepskyblue;'></i> </a>".format(
            obj.mobile_no)
        return format_html(buttons)

    Call.short_description = " "

    def SMS(self, obj):
        buttons = ''
        buttons += "<a href='sms:+91{}' target='_blank'> <i class='fa fa-commenting-o' style='font-size:27px;color:lightblue;'></i> </a>".format(
            obj.mobile_no)
        return format_html(buttons)

    SMS.short_description = " "

    class Media:
        css = {'all': ("client_side_image_cropping/croppie.css", "client_side_image_cropping/cropping_widget.css",)}
        js = ("client_side_image_cropping/croppie.min.js", "client_side_image_cropping/cropping_widget.js",)


class SantRead(Sant):
    class Meta:
        proxy = True
        verbose_name_plural = "પૂ.સંત વિગત"
        verbose_name = "પૂ.સંત વિગત"


class SantProxiAdmin(SantAdmin):
    readonly_fields = ('Name', 'english_name', 'mobile_no','remark')
    inlines = [PurvashramDetailsInline, DikshaDetailsInline, AnuvrutiDetailsInline, AttachmentsReadInline]
    class Media:
        css = {'all': ("client_side_image_cropping/croppie.css", "client_side_image_cropping/cropping_widget.css",)}
        js = ("client_side_image_cropping/croppie.min.js", "client_side_image_cropping/cropping_widget.js",)


admin.site.register(Sant, SantAdmin)
admin.site.register(SantRead, SantProxiAdmin)
