from django.contrib.postgres import search
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from project.models import Project, Manager, Contractor, Gantt, Budget, Image


# Display list of Projects
class ProjectList(ListView):
    model = Project
    context_object_name = 'project'


# Display Gantt by Project
class ProjectGanttList(ListView):
    context_object_name = 'gantt'

    # Get the Gantts by Project
    def get_queryset(self):
        self.project = get_object_or_404(
            Project, name=self.kwargs['project'])
        return Gantt.objects.filter(project=self.project)

    # Get the Project
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

# Display one Project with the lastest Images and Gantt


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    gantt = Gantt.objects.filter(project_id=project_id).latest('report_date')
    image = Image.objects.filter(project_id=project_id).latest('list_date')
    budget = Budget.objects.filter(project_id=project_id).latest('create_date')
    #image = get_object_or_404(Image,project_id=project_id).latest('list_date')
    #gantt= get_object_or_404(Gantt, project_id=project_id).latest('report_date')

    context = {'project': project,
               'gantt': gantt,
               'image': image,
               'budget': budget, }

    return render(request, 'project/project.html', context)


def index(request):
    projects = Project.objects.order_by(
        '-create_date').filter(is_published=True)

    paginator = Paginator(projects, 3)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    #ganttimage = GanttImage.objects.filter(project_id=projects.id).lates('reporte_date')
    context = {
        'projects': paged_projects,
    }
    return render(request, 'project/projects.html', context)


def search(request):
    queryset_list = Project.objects.order_by('-create_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Term of work, goal_time
    if 'goal_time' in request.GET:
        goal_time = request.GET['goal_time']
        if goal_time:
            queryset_list = queryset_list.filter(goal_time__lte=goal_time)

    # Budget allocated
    if 'budget_allocated' in request.GET:
        budget_allocated = request.GET['budget_allocated']
        if budget_allocated:
            queryset_list = queryset_list.filter(
                budget_allocated__lte=budget_allocated)

    # Scope of Project (i.e design, fuels, image)
    if 'scope' in request.GET:
        scope = request.GET['scope']
        if scope:
            queryset_list = queryset_list.filter(scope__iexact=scope)

    context = {
        'state_choices': state_choices,
        'budget_choices': budget_choices,
        'scope_choices': scope_choices,
        'goaltime_choices': goaltime_choices,
        'projects': queryset_list,
        'values': request.GET
    }
    return render(request, 'project/search.html', context)
