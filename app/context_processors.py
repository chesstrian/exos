def menu(request):
    _menu = dict(
        menu_home='',
        menu_list='',
        menu_add='',
        menu_view='',
        menu_edit='',
        menu_delete='',
    )

    if '/list' in request.path:
        _menu['menu_list'] = 'active'
    elif '/add' in request.path:
        _menu['menu_add'] = 'active'
    elif '/view' in request.path:
        _menu['menu_view'] = 'active'
    elif '/edit' in request.path:
        _menu['menu_edit'] = 'active'
    elif '/delete' in request.path:
        _menu['menu_delete'] = 'active'
    else:
        _menu['menu_home'] = 'active'

    return _menu
