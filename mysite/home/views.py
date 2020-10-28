from django import generic
from . import models
from django
from django.contrib.auth.decorators import login_required


@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=Page.slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'home/product.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})


@login_required
@register.simple_tag()
def post_date_url(post, blog_page):
    post_date = post.date
    url = blog_page.url + blog_page.reverse_subpage(
        'post_by_date_slug',
        args=(
            post_date.year,
            '{0:02}'.format(post_date.month),
            '{0:02}'.format(post_date.day),
            post.slug,
        )
    )
    return url

@login_required
@register.inclusion_tag('blog/comments/disqus.html', takes_context=True)
def show_comments(context):
    blog_page = context['blog_page']
    post = context['post']
    path = post_date_url(post, blog_page)

    raw_url = context['request'].get_raw_uri()
    parse_result = six.moves.urllib.parse.urlparse(raw_url)
    abs_path = six.moves.urllib.parse.urlunparse([
        parse_result.scheme,
        parse_result.netloc,
        path,
        "",
        "",
        ""
    ])

    return {'disqus_url': abs_path,
            'disqus_identifier': post.pk,
            'request': context['request']}