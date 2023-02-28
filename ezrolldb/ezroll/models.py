from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    duid = models.CharField(max_length=9)
    major = models.CharField(max_length=100)
    minor = models.CharField(max_length=100)
    PoCRN = models.CharField(max_length=100)
    PrCRN = models.CharField(max_length=100)
    elec = models.CharField(max_length=100)

def __str___(self):
    return self.name + ' '

class Course(models.Model):
    TERM_CODE= models.CharField(max_length=255)
    CRN= models.IntegerField()
    TERM_DESC= models.CharField(max_length=255)
    SUBJ_CODE= models.CharField(max_length=255)
    SUBJ_DESC= models.CharField(max_length=255)
    CRSE_NUM= models.CharField(max_length=255)
    SEQ_NUM= models.CharField(max_length=255)
    XLST_GROUP= models.CharField(max_length=255)
    MAX_ENRL= models.CharField(max_length=255)
    CREDIT_HR= models.CharField(max_length=255)
    COLL_DESC= models.CharField(max_length=255)
    DEPT_DESC= models.CharField(max_length=255)
    BLDG_DESC= models.CharField(max_length=255)
    ROOM_CODE= models.CharField(max_length=255)
    BEGIN_TIME= models.CharField(max_length=255)
    END_TIME= models.CharField(max_length=255)
    START_DATE= models.CharField(max_length=255)
    END_DATE= models.CharField(max_length=255)
    SUN_DAY= models.CharField(max_length=20)
    MON_DAY= models.CharField(max_length=20)
    TUE_DAY= models.CharField(max_length=20)
    WED_DAY= models.CharField(max_length=20)
    THU_DAY= models.CharField(max_length=20)
    FRI_DAY= models.CharField(max_length=20)
    SAT_DAY= models.CharField(max_length=20)
    HRS_WEEK= models.CharField(max_length=20)  
    
    def __str___(self):
        return self.CRN + ' '+ self.SUBJ_CODE
    
