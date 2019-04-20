from django.shortcuts import get_object_or_404
from notes.models import Note
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .mixins import LoginRequiredMixin, NoteMixin
from django.utils import timezone 
from django.urls import reverse_lazy, reverse

from .forms import NoteForm


'''@login_required
def index(request):
    latest_note_list = Note.objects.filter(owner=request.user).order_by('-pub_date')[:5]
    context = {
        'latest_note_list' : latest_note_list
    }
    return render(request, 'notes/index.html', context)

@login_required
def detail(request, note_id):
    note = get_object_or_404(Note, pk = note_id, owner = request.user)
    return render(request, 'notes/detail.html', {'note':note})'''


# Вместо вьюх выше используем class-based views 


class NoteList(LoginRequiredMixin, ListView):
	paginate_by = 5
	template_name = 'notes/index.html'
	context_object_name = 'latest_note_list'

	def get_queryset(self):
		return Note.objects.filter(owner = self.request.user).order_by('-pub_date')


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


class NoteCreate(LoginRequiredMixin, NoteMixin, CreateView):
    form_class = NoteForm
    template_name = 'notes/form.html'
    success_url = reverse_lazy('notes:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.pub_date = timezone.now()
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, NoteMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/form.html'

    def get_queryset(self):
        return Note.objects.filter(owner = self.request.user)

    def get_success_url(self):
        return reverse('notes:update', kwargs = {'pk':self.object.pk})


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:create')

    def get_queryset(self):
        return Note.objects.filter(owner = self.request.user)

