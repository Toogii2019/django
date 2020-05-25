from django.contrib import admin
from polling.models import Poll
from blogging.models import Category, Post


class MembershipInline(admin.TabularInline):
    model = Category.posts.through
    extra = 0
    pass


class PostAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ("posts",)


admin.site.site_header = "Django Blog Admin"
admin.site.site_title = "Django Blog Title"
admin.site.index_title = "Django Blog Index"

# admin.site.register(PostAdmin)
# admin.site.register(CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Poll)
# admin.site.register(Post)
# admin.site.register(Category)
