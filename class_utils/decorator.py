from elearning.settings import PAGE_PERMISSION_DENIED, LIST_PERMISSION, LOGIN_PAGE
from django.shortcuts import redirect, render


def is_in_group(redirect_template=None, group=None, only_admin=None):

    """
    use: is_in_group( group='vpn' )
    check if user is_authenticated and is in group described

	use: is_in_group( )
	group not define but if you are authenticated and you are administrator pass check. 

    """
    if redirect_template is None:
        redirect_template = PAGE_PERMISSION_DENIED

    def _dec(view_func):
        def _view(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect('%s?next=%s' % (LOGIN_PAGE, request.path))

            if only_admin is None:
                pass
            else:
                if request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
                else:
                    return render(request, redirect_template, )

            if group is None:

                if request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
                else:
                    return render(request, redirect_template, )

            else:
                group_inside_dec = LIST_PERMISSION[group]

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            else:
                if request.user:
                    if request.user.groups.filter(name=group_inside_dec).count() == 1:
                        return view_func(request, *args, **kwargs)

            return render(request, redirect_template, )

        return _view

    return _dec
