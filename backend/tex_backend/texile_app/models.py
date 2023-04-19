import email
from pyexpat import model
from statistics import mode
from time import time
from xml.etree.ElementTree import Comment
from django.db import models
from datetime import datetime
from model_utils import Choices

choices = ('Scrap','HRC','STLD','RS','CLF','TX','GGB','X','CMC','TS','VK.PA','TMST','MT','PKX','NUE','RIO','VALE','SXC','BHP','HO=F','RB=F','coal','NWPX','TKA.DE','SZG.DE','Nippon','JFE','iron','ULSD','BADI','Truck','CassFreight')
index_choices= ('raw material index','pipe manufacturing','steel manufacturing','iron ore mining','fuel','transport')
mychoices = ('Scrap','HRC','STLD','RS','CLF','TX','GGB','X','CMC','TS','VK.PA','TMST','MT','PKX','NUE','RIO','VALE','SXC','BHP','HO=F','RB=F','coal','NWPX','TKA.DE','SZG.DE','Nippon','JFE','iron','ULSD','BADI','Truck','CassFreight','AllGrade','Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC','raw material index','pipe manufacturing','steel manufacturing','iron ore mining','fuel','transportation', 'RC_index', 'DPR_DUC')


# Create your models here.
class stock_data(models.Model):
    chart_type = models.CharField(max_length=20, default="")
    data = models.FloatField()
    current = models.FloatField()

class yahoo_data(models.Model):
    chart = models.CharField(max_length=10, default="")
    chart_type = models.CharField(max_length=10, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=10, default="")

class transportation_data(models.Model):
    chart = models.CharField(max_length=20, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=10, default="")

class rmi_data(models.Model):
    chart = models.CharField(max_length=20, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=10, default="")

class future_yahoo_data(models.Model):
    chart = models.CharField(max_length=10, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=10, default="")

class market_cap_data(models.Model):
    chart = models.CharField(max_length=20, default="")
    # chart_type = models.CharField(max_length=10, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=10, default="")

class index_data(models.Model):
    chart = models.CharField(max_length=20, default="")
    # chart_type = models.CharField(max_length=10, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=10, default="")

class index_pmf_data(models.Model):
    date = models.CharField(max_length=10, default="")
    TS = models.CharField(max_length=20, default="")
    VKPA = models.CharField(max_length=20, default="")
    X = models.CharField(max_length=20, default="")
    TMST = models.CharField(max_length=20, default="")
    NWPX = models.CharField(max_length=20, default="")
    PMF_index = models.CharField(max_length=20, default="")

class index_smf_data(models.Model):
    date = models.CharField(max_length=10, default="")
    MT = models.CharField(max_length=20, default="")
    PKX = models.CharField(max_length=20, default="")
    NUE = models.CharField(max_length=20, default="")
    STLD = models.CharField(max_length=20, default="")
    RS = models.CharField(max_length=20, default="")
    CLF = models.CharField(max_length=20, default="")
    TX = models.CharField(max_length=20, default="")
    GGB = models.CharField(max_length=20, default="")
    X = models.CharField(max_length=20, default="")
    CMC = models.CharField(max_length=20, default="")
    TKADE = models.CharField(max_length=20, default="")
    SZGDE = models.CharField(max_length=20, default="")
    NIPPON = models.CharField(max_length=20, default="")
    JFE = models.CharField(max_length=20, default="")
    SMF_index = models.CharField(max_length=20, default="")

class index_iom_data(models.Model):
    date = models.CharField(max_length=10, default="")
    RIO = models.CharField(max_length=20, default="")
    VALE = models.CharField(max_length=20, default="")
    SXC = models.CharField(max_length=20, default="")
    BHP = models.CharField(max_length=20, default="")
    IOM_index = models.CharField(max_length=20, default="")

class index_f_data(models.Model):
    date = models.CharField(max_length=10, default="")
    HO = models.CharField(max_length=20, default="")
    RB = models.CharField(max_length=20, default="")
    F_index = models.CharField(max_length=20, default="")

class index_rmi_data(models.Model):
    date = models.CharField(max_length=10, default="")
    SCRAP = models.CharField(max_length=20, default="")
    HRC = models.CharField(max_length=20, default="")
    COAL = models.CharField(max_length=20, default="")
    IRONORE = models.CharField(max_length=20, default="")
    RMI_index = models.CharField(max_length=20, default="")

class index_rmi_cme_data(models.Model):
    date = models.CharField(max_length=10, default="")
    SCRAP = models.CharField(max_length=20, default="")
    HRC = models.CharField(max_length=20, default="")
    COAL = models.CharField(max_length=20, default="")
    IRONORE = models.CharField(max_length=20, default="")
    RMI_index = models.CharField(max_length=20, default="")

class index_t_data(models.Model):
    date = models.CharField(max_length=10, default="")
    ULSD = models.CharField(max_length=20, default="")
    BALTIC = models.CharField(max_length=20, default="")
    ALLGRADE = models.CharField(max_length=20, default="")
    T_index = models.CharField(max_length=20, default="")

class index_rig_data(models.Model):
    date = models.CharField(max_length=10, default="")
    Ardmore	= models.CharField(max_length=20, default="")
    Arkoma = models.CharField(max_length=20, default="")
    Barnett	= models.CharField(max_length=20, default="")
    Cana = models.CharField(max_length=20, default="")
    Niobrara = models.CharField(max_length=20, default="")
    Ford = models.CharField(max_length=20, default="")
    Granite	= models.CharField(max_length=20, default="")
    Haynesville	= models.CharField(max_length=20, default="")
    Marcellus = models.CharField(max_length=20, default="")
    Mississippian = models.CharField(max_length=20, default="")
    Permian	= models.CharField(max_length=20, default="")
    Utica = models.CharField(max_length=20, default="")
    Williston = models.CharField(max_length=20, default="")
    RC_index = models.CharField(max_length=20, default="")

class index_duc_data(models.Model):
    date = models.CharField(max_length=10, default="")
    Anadarko_D = models.CharField(max_length=20, default="")
    Anadarko_C = models.CharField(max_length=20, default="")
    Anadarko_DUC = models.CharField(max_length=20, default="")
    Appalachia_D = models.CharField(max_length=20, default="")
    Appalachia_C = models.CharField(max_length=20, default="")
    Appalachia_DUC = models.CharField(max_length=20, default="")
    Bakken_D	= models.CharField(max_length=20, default="")
    Bakken_C	= models.CharField(max_length=20, default="")
    Bakken_DUC	= models.CharField(max_length=20, default="")
    Eagle_D = models.CharField(max_length=20, default="")
    Eagle_C = models.CharField(max_length=20, default="")
    Eagle_DUC = models.CharField(max_length=20, default="")
    Haynesville_D = models.CharField(max_length=20, default="")
    Haynesville_C = models.CharField(max_length=20, default="")
    Haynesville_DUC = models.CharField(max_length=20, default="")
    Niobrara_D = models.CharField(max_length=20, default="")
    Niobrara_C = models.CharField(max_length=20, default="")
    Niobrara_DUC = models.CharField(max_length=20, default="")
    Permian_D = models.CharField(max_length=20, default="")
    Permian_C = models.CharField(max_length=20, default="")
    Permian_DUC = models.CharField(max_length=20, default="")
    DPR_D	= models.CharField(max_length=20, default="")
    DPR_C	= models.CharField(max_length=20, default="")
    DPR_DUC	= models.CharField(max_length=20, default="")

class daily_index(models.Model):
    chart = models.CharField(max_length=30, default="")
    date = models.CharField(max_length=10, default="")
    val = models.CharField(max_length=10, default="")
    update_time = models.CharField(max_length=30, default="")

class hourly_index(models.Model):
    chart = models.CharField(max_length=30, default="")
    date = models.CharField(max_length=10, default="")
    val = models.CharField(max_length=10, default="")
    update_time = models.CharField(max_length=30, default="")

class hourly_yahoo_data(models.Model):
    chart = models.CharField(max_length=30, default="")
    date = models.CharField(max_length=10, default="")
    val = models.CharField(max_length=10, default="")
    update_time = models.CharField(max_length=30, default="")

class emails(models.Model):
    email = models.CharField(max_length=200, default="")
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")

class changelogs(models.Model):
    changelog = models.CharField(max_length=10000, default="")
    version = models.CharField(max_length=10, default="")
    app = models.CharField(max_length=10, default="")
    os = models.CharField(max_length = 20, default="")

class updated_time(models.Model):
    chart = models.CharField(max_length=30, default="")
    update_time = models.DateTimeField(default=datetime.now, blank=True)

class customer_table(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    Terms = models.CharField(max_length=5, default="N")
    user = models.CharField(max_length=40, default="")
    vr = models.CharField(max_length=40, default="")
    os = models.CharField(max_length=40, default="")
    emailID = models.CharField(max_length=100, default="")
    terms_vr = models.CharField(max_length=40, default="")
    first_installed_vr = models.CharField(max_length=40, default="")

class version_info(models.Model):
    version = models.CharField(max_length = 10)
    app = models.CharField(max_length = 10)
    url = models.CharField(max_length = 100)
    os = models.CharField(max_length = 20, default="")
    terms_vr = models.CharField(max_length=40, default="")


#############Usage metric tables#################
class chart_usage(models.Model):
    chart = models.CharField(max_length=30, default="")
    visits = models.IntegerField()

class device_chart_usage(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    chart = models.CharField(max_length=30, default="")
    visits = models.IntegerField()

class device_session_chart_usage(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    session_id =  models.CharField(max_length=40, default="")
    chart = models.CharField(max_length=30, default="")
    visits = models.IntegerField()
    created_time = models.DateTimeField(default=datetime.now, blank=True)

class session_usage(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    session_id =  models.CharField(max_length=40, default="")
    time = models.CharField(max_length=40, default="")
    created_time = models.DateTimeField(default=datetime.now, blank=True)

class session_page_usage(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    session_id =  models.CharField(max_length=40, default="")
    landing_page = models.CharField(max_length=40, default="0")
    rmi_page = models.CharField(max_length=40, default="0")
    iom_page = models.CharField(max_length=40, default="0")
    t_page = models.CharField(max_length=40, default="0")
    pmf_page = models.CharField(max_length=40, default="0")
    smf_page = models.CharField(max_length=40, default="0")
    carbon_offset = models.CharField(max_length=40, default="0")

class session_page_usage_new(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    session_id =  models.CharField(max_length=40, default="")
    landing_page = models.CharField(max_length=40, default="0")
    rmi_page = models.CharField(max_length=40, default="0")
    iom_page = models.CharField(max_length=40, default="0")
    t_page = models.CharField(max_length=40, default="0")
    pmf_page = models.CharField(max_length=40, default="0")
    smf_page = models.CharField(max_length=40, default="0")
    rc_page = models.CharField(max_length=40, default="0")
    wc_page = models.CharField(max_length=40, default="0")
    carbon_offset = models.CharField(max_length=40, default="0")
    watchlist = models.CharField(max_length=40, default="0")
    feedback = models.CharField(max_length=40, default="0")
    about = models.CharField(max_length=40, default="0")
    tutorial = models.CharField(max_length=40, default="0")

class device_page_clicks(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length=40, default="")
    session_id =  models.CharField(max_length=40, default="")
    landing_page = models.CharField(max_length=40, default="0")
    rmi_page = models.CharField(max_length=40, default="0")
    iom_page = models.CharField(max_length=40, default="0")
    t_page = models.CharField(max_length=40, default="0")
    pmf_page = models.CharField(max_length=40, default="0")
    smf_page = models.CharField(max_length=40, default="0")
    rc_page = models.CharField(max_length=40, default="0")
    wc_page = models.CharField(max_length=40, default="0")
    carbon_offset = models.CharField(max_length=40, default="0")
    watchlist = models.CharField(max_length=40, default="0")
    feedback = models.CharField(max_length=40, default="0")
    about = models.CharField(max_length=40, default="0")
    tutorial = models.CharField(max_length=40, default="0")
    created_time = models.DateTimeField(default=datetime.now, blank=True)
#################################################

class website_viewers(models.Model):
    email_id = models.CharField(max_length = 300)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    config = models.TextField(max_length=20000, default="")

class carbon_factor(models.Model):
    product = models.CharField(max_length = 20, default="")
    factor = models.CharField(max_length=20, default="")

class watchlist(models.Model):
    app = models.CharField(max_length=10, default="")
    deviceID = models.CharField(max_length = 300)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    config = models.TextField(max_length=20000, default="")
    
class feedback(models.Model):
    deviceID = models.CharField(max_length = 300)
    Name = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)
    PhoneNo = models.CharField(max_length = 10)
    Comment = models.CharField(max_length = 1000)
    Rating = models.CharField(max_length = 2)
    app = models.CharField(max_length = 10)
    created_time = models.DateTimeField(default=datetime.now, blank=True)

class customMessage(models.Model):
    app = models.CharField(max_length = 10)
    title = models.CharField(max_length = 100)
    message = models.CharField(max_length=100000, default="")
    # def __str__(self):
    #     return f"{self.title}+{self.message}"
class y_data_ts(models.Model):
    chart_type = models.CharField(max_length=10, default="")
    data = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=20, default="")
    time=models.CharField(max_length=50,default="")

################Tweet Tables################
class tweet_table_ticker_test(models.Model):
    tweet_link = models.CharField(max_length=100, default="")
    html = models.TextField(max_length=2000, default="")
    author_name = models.TextField(max_length=200, default="")
    author_url = models.TextField(max_length=200, default="")
    profile_pic = models.TextField(max_length=200, default="")
    image_url = models.TextField(max_length=200, default="")
    web_url = models.TextField(max_length=200, default="")
    web_url_image = models.TextField(max_length=200, default="")
    web_text = models.TextField(max_length=200, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    tab_name = models.CharField(max_length = 20, choices = Choices(*choices), default = "")
    relevance_level_tab = models.IntegerField(default="99")
    on_landing_page = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    relevance_level_landing_page = models.IntegerField(default="99")
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    actual_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    predicted_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    class Meta:
        verbose_name_plural = "Ticker Level Tweets Test"

class tweet_table_index_test(models.Model):
    tweet_link = models.CharField(max_length=100, default="")
    html = models.TextField(max_length=2000, default="")
    author_name = models.TextField(max_length=200, default="")
    author_url = models.TextField(max_length=200, default="")
    profile_pic = models.TextField(max_length=200, default="")
    image_url = models.TextField(max_length=200, default="")
    web_url = models.TextField(max_length=200, default="")
    web_url_image = models.TextField(max_length=200, default="")
    web_text = models.TextField(max_length=200, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    chart = models.CharField(max_length=200, choices= Choices(*index_choices) ,default="")
    relevance_level = models.IntegerField(default="99")
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    actual_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    predicted_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    class Meta:
        verbose_name_plural = "Index Level Tweets Test"

class tweet_table_ticker(models.Model):
    tweet_link = models.CharField(max_length=100, default="")
    html = models.TextField(max_length=2000, default="")
    author_name = models.TextField(max_length=200, default="")
    author_url = models.TextField(max_length=200, default="")
    profile_pic = models.TextField(max_length=200, default="")
    image_url = models.TextField(max_length=200, default="")
    web_url = models.TextField(max_length=200, default="")
    web_url_image = models.TextField(max_length=200, default="")
    web_text = models.TextField(max_length=200, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    tab_name = models.CharField(max_length = 20, choices = Choices(*choices), default = "")
    relevance_level_tab = models.IntegerField(default="99")
    on_landing_page = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    relevance_level_landing_page = models.IntegerField(default="99")
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    actual_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    predicted_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    class Meta:
        verbose_name_plural = "Ticker Level Tweets Test"

class tweet_table_index(models.Model):
    tweet_link = models.CharField(max_length=100, default="")
    html = models.TextField(max_length=2000, default="")
    author_name = models.TextField(max_length=200, default="")
    author_url = models.TextField(max_length=200, default="")
    profile_pic = models.TextField(max_length=200, default="")
    image_url = models.TextField(max_length=200, default="")
    web_url = models.TextField(max_length=200, default="")
    web_url_image = models.TextField(max_length=200, default="")
    web_text = models.TextField(max_length=200, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    chart = models.CharField(max_length=200, choices= Choices(*index_choices) ,default="")
    relevance_level = models.IntegerField(default="99")
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    actual_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    predicted_relevant = models.CharField(max_length=2, choices = (("R","R"),("NR","NR"),("U","U")),default="U")
    class Meta:
        verbose_name_plural = "Index Level Tweets Test"


############News Tables#####################
class News_test(models.Model):
     # TabNo = models.CharField(max_length = 5, choices = (("Tab1", "Tab1"),("Tab2", "Tab2")), default = "Tab1")
    chart = models.CharField(max_length=200, choices= Choices(*index_choices) ,default="")
    relevance_level = models.IntegerField(default="99")
    title = models.CharField(max_length = 1000, default="")
    link = models.CharField(max_length = 1000)
    website = models.CharField(max_length = 1000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.TextField(max_length = 500, blank=True)
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    class Meta:
        verbose_name_plural = "Index Level News"

class News_data_test(models.Model):
    tab_name = models.CharField(max_length = 20, choices = Choices(*choices), default = "")
    relevance_level_tab = models.IntegerField(default="99")
    on_landing_page = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    relevance_level_landing_page = models.IntegerField(default="99")
    title = models.CharField(max_length = 1000, default="")
    link = models.CharField(max_length = 1000)
    website = models.CharField(max_length = 1000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.TextField(max_length = 500, blank=True) 
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    class Meta:
        verbose_name_plural = "Ticker Level News" 

class News(models.Model):
     # TabNo = models.CharField(max_length = 5, choices = (("Tab1", "Tab1"),("Tab2", "Tab2")), default = "Tab1")
    chart = models.CharField(max_length=200, choices= Choices(*index_choices) ,default="")
    relevance_level = models.IntegerField(default="99")
    title = models.CharField(max_length = 1000, default="")
    link = models.CharField(max_length = 1000)
    website = models.CharField(max_length = 1000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.TextField(max_length = 500, blank=True)
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    class Meta:
        verbose_name_plural = "Index Level News"

class News_data(models.Model):
    tab_name = models.CharField(max_length = 20, choices = Choices(*choices), default = "")
    relevance_level_tab = models.IntegerField(default="99")
    on_landing_page = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    relevance_level_landing_page = models.IntegerField(default="99")
    title = models.CharField(max_length = 1000, default="")
    link = models.CharField(max_length = 1000)
    website = models.CharField(max_length = 1000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.TextField(max_length = 500, blank=True) 
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    word_count = models.IntegerField(default="0")
    class Meta:
        verbose_name_plural = "Ticker Level News" 

class News_rec(models.Model):
    tab_name = models.CharField(max_length = 20, choices = Choices(*mychoices), default = "")
    relevance_level_tab = models.IntegerField(default="99")
    on_landing_page = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    relevance_level_landing_page = models.IntegerField(default="99")
    title = models.CharField(max_length = 1000, default="")
    link = models.CharField(max_length = 1000)
    website = models.CharField(max_length = 1000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.TextField(max_length = 500, blank=True) 
    archive = models.CharField(max_length=1, choices = (("Y","Y"),("N","N")),default="N")
    exp_date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        verbose_name_plural = "Overriding News" 
######################################################################################################

