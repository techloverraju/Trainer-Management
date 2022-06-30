from django.urls import path

from Trainerapp import views

urlpatterns=[
    path('',views.home,name='home'),        # it will display index.html.
    path('logread',views.log_read),

    path('register',views.trainer_register,name='reg'),    # to rediect to trainer_reg.html page.
    path('trainerreg',views.register_data),
    path('trainerhome',views.trainer_home,name='thome'),
    path('trainerbatch',views.trainer_batch,name='tbatch'),

    path('adminhome',views.admin_home,name='adminhome'),    # it will redirect to admin_home.html page
    path('trainerdet',views.triner_details,name='triner_details'), # it will retrive data from Trainer_register model and redirect to trainer_details.html page.
    path('trainerassign',views.trainer_assign,name='trainerassign'),  # it will display trainerassign.html page.
    path('assign',views.assign_batch),                       # it will read the data and store it in trainer_assign model/trainer.
    path('details',views.batch_details,name='details'),       # it will display all the trainer_batch details
    path('delete/<int:id>',views.delete_batch,name='del'),      # it will delete the batch
    path('update/<int:id>',views.update_batch,name='up'),       # it will update particular record.
]