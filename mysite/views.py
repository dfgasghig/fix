from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Review
from .forms import PostForm, EditForm, RateForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_time']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        casting_rates = Review.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["casting_rates"] = casting_rates
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        casting_rates = Review.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["casting_rates"] = casting_rates
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

def SearchPosts(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Post.objects.all().filter(title = search)
        return render(request, 'search_things.html', {'post': post})

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def RateView(request, pk):
    post = Post.objects.get(id = pk)
    user = request.user

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit = False)
            rate.user = user
            rate.post = post
            rate.save()
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        form = RateForm()

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'rate_post.html', context)