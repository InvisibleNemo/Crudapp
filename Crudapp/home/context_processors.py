def user_info(request):
    user = request.user
    if user.is_authenticated:
        user_info = {
            'user_first_name': user.first_name if user.first_name else 'FNU',
            'user_last_name': user.last_name if user.last_name else 'LNU',
        }
        return user_info
    else:
        return ''
