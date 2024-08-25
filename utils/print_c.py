def print_c(arr):
    html = ''
    for item in arr:
        html += f'<div>{{{item}}}</div>'
    return html
