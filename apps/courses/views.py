from django.shortcuts import render, redirect, HttpResponse
import models

def index(request):
    course = models.Course.objects.all()
    description = models.Description.objects.all()
    context = {
        'courses' : course,
        'descriptions' : description
     }
    print ('*'*97)+' ABOUT TO RETURN index.html '+('*'*97)
    return render(request, 'courses/index.html', context)

def add_course_path(request):
    if request.POST['course_name']:
        print ('*'*102)+' Adding course... '+('*'*102)
        course = models.Course.objects.create( course_name = request.POST['course_name'] )
        print "THIS IS THE COURSE THING",course,"!!!!!!!!"
        description = models.Description.objects.create( course = course, text = request.POST['description'] )
        checkC = models.Course.objects.all()
        checkD = models.Description.objects.all()
        print checkC
        print checkD
        print ('*'*98)+' ADDED COURSE TO DATABASE '+('*'*98)
    return redirect('/')

def remove(request, course_id):
    victimC = models.Course.objects.get( id = course_id )
    victimC.delete()
    try:
        victimD = models.Description.objects.get( course = course_id )
        if victimD :
            victimD.delete()
    except:
        pass
    print ('*'*101)+' Removing course... '+('*'*101)
    return redirect('/')

def add_comment_path(request, course_id):
    course = models.Course.objects.get( id = course_id )
    comment = models.Comment.objects.create( text = request.POST['comment'], course = course )
    ('*'*101)+' Adding comment... '+('*'*101)
    return redirect('/comments_for_'+course_id)

def comments_for(request, course_id):
    course = models.Course.objects.get( id = course_id )
    comments = models.Comment.objects.filter( course = course )
    context = {
        'comments' : comments,
        'course' : course
    }
    print ('*'*97)+' ABOUT TO RETURN comments.html '+('*'*97)
    return render(request, 'courses/comments.html', context)

def comments_for(request, course_id):
    course = models.Course.objects.get( id = course_id )
    comments = models.Comment.objects.filter( course = course )
    context = {
        'comments' : comments,
        'course' : course
    }
    print ('*'*97)+' ABOUT TO RETURN comments.html '+('*'*97)
    return render(request, 'courses/comments.html', context)

def delete_check(request, course_id):
    course = models.Course.objects.get( id = course_id )
    description = models.Description.objects.filter( course = course )
    context = {
        'description' : description,
        'course' : course
    }
    print ('*'*97)+' ABOUT TO RETURN delete_check.html '+('*'*97)
    return render(request, 'courses/delete_confirm.html', context)
