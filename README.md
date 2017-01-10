# National Parks

The National Park Service was created in 1916 by President Woodrow Wilson in order to preserve America's natural and historic scenery. The NPS oversees over 400 units of preserves, monuments, battlefields, and parks. 59 of these units are officially designated as National Parks.

Let's create an app to showcase these wonderful parks.

## Getting Started

Fork and clone this repository
Follow the recommended process for creating your Django app.

## Components

### Models
A Park model that stores the following attributes. Choose the appropriate data
types for each (string or text) 
- name
- description
- picture (for now, have this store a URL to a picture of a park)

### Controllers
- A controller for your home page
- A controller for your `Park` model

### Routes and Views
| Route             | Description                    | Controller | Action/View       |
| -------           | -----                          | ----       | -----             |
| GET /             | Your home page                 | home       | index             |
| GET /parks        | list all parks                 | parks      | index             |
| GET /parks/new    | show add park form             | parks      | new               |
| POST /parks       | create park                    | parks      | create (no view)  |
| GET /parks/1      | list park (id=1)               | parks      | show              |
| GET /parks/2/edit | show edit park form (id=2)     | parks      | edit              |
| PUT /parks/3      | update an existing park (id=3) | parks      | update (no view)  |
| DELETE /parks/3   | delete an existing park (id=3) | parks      | destroy (no view) |

### Recommended Process
#### Create basic app
- fork and clone this repo
- cd into the directory
- create Django project `django-admin startproject parks_site`
- create app in project `python3 manage.py parks`
- run the server! `python3 manage.py runserver` 

#### Build Specific Functionality
Define a view in parks/views.py

```py
from django.http import HttpResponse

def index(request):
  return HttpResponse("This will become a list of all Parks.")
```

Create a route in  the parks app `parks/urls.py`:

```py
from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
]
```

Attach the parks app to the main site by defining how URLs are routed to it
in `parks_site/urls.py`:

```py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^parks/', include('parks.urls')),
  url(r'^admin/', admin.site.urls),
]
```

Run the server and verify that everything is wired up correctly by visiting
<http://localhost:8000/parks/>

### Styling
- Style the pages. Play around with adding a navigation bar or carousels.
- If using Bootstrap, use the Bootstrap form helper. Makes Bootstrap forms easily.

### Bonuses
- Create a seed file to load some National Parks
- Replace the URL links with Cloudinary uploads.

---

## Licensing
1. All content is licensed under a CC-BY-NC-SA 4.0 license.
2. All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.
