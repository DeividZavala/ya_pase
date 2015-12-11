# from .models import UserProfile
# from django.utils.six.moves import urllib
# from django.utils.six import BytesIO

# def save_profile_picture(
# 	backend, user, response, 
# 	details,is_new=False,*args,**kwargs):
# 	if backend.__class__.__name__ == 'FacebookOAuth2':
# 		up = UserProfile.objects.get_or_create(user=user) #RETURNS TUPLE (instance, created(boolean))
# 		if not up[0].photo:
# 			url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
# 			response = urllib.request.urlopen(url)
# 			io = BytesIO(response.read())
# 			up[0].photo.save('profile_pic_{}.jpg'.format(user.pk), File(io))
# 			up[0].save() 

# from requests import request, HTTPError

# from django.core.files.base import ContentFile


# def save_profile_picture(strategy, user, response, details,
#                          is_new=False,*args,**kwargs):
# 	if is_new and strategy.backend.__class__.__name__ == 'FacebookOAuth2':
# 		url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
# 		try:
# 			response = request('GET', url, params={'type': 'large'})
# 			response.raise_for_status()
# 		except HTTPError:
# 			pass
# 		else:
# 			# profile = user.get_profile()
# 			profile=UserProfile.objects.get_or_create(user=user)
# 			profile.photo.save('{0}_social.jpg'.format(user.username),
# 				ContentFile(response.content))
# 			profile.save()



from django.core.files.base import ContentFile
from requests import request, ConnectionError
from .models import UserProfile
from django.contrib.auth.models import User


def save_profile_picture(backend, user, response, is_new,  *args, **kwargs):
    '''
    Get the user avatar (and any other details you're interested in)
    and save them to the userprofile
    '''
    if backend.name == 'google-plus':  
        if response.get('image') and response['image'].get('url'):
            url = response['image'].get('url')
            prof=UserProfile.objects.get_or_create(user=user)
            if prof.avatar:
                # if existing avatar stick with it rather than google syncing
                pass
            else:
                try:
                    response = request('GET', url)
                    response.raise_for_status()
                except ConnectionError:
                    pass
                else:
                    # No avatar so sync it with the google one.
                    # Passing '' for name will invoke my upload_to function
                    # saving by username (you prob want to change this!)
                    prof.avatar.save(u'',
                                    ContentFile(response.content),
                                    save=False
                                    )
                    prof.save()
    elif backend.name == 'facebook' and is_new:
        # prof=UserProfile.objects.get_or_create(user=user)
        # prof1=User.objects.get(username=user.username)
        print ("Antes:",user)
        user_model=user
        # user_profile=UserProfile.objects.get_or_create(user=user)
        user_profile=UserProfile()
        user_profile.user=user_model
        print (user_profile,"despues",user_model)
        # user_profile.user=user_model

        if user_profile.photo:
            pass
        else:
            url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

            try:
                response = request('GET', url, params={'type': 'large'})
                response.raise_for_status()
            except ConnectionError:
                pass
            else:
            	# user_profile.photo=photo
            	user_profile.photo.save(u'',
                                 ContentFile(response.content),
                                 save=False
                                 )
            	user_profile.save()
               