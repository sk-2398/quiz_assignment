
from django.shortcuts import redirect, render
from .models import Quiz

import random
# Create your views here.


def check(n1,n2):
    if n1==n2:
        return True
    


def home(request):
    return render(request,'home.html')

def questions():
    return Quiz.objects.order_by('?')[:5]

# quiz_obj=list(Quiz.objects.all())
# question_list=random.sample(quiz_obj,5)
   

question_list=list(questions())

li=[]
def quiz(request):
    q_no=int(request.GET.get('next'))
    choice=request.GET.get('choice')
    print(choice)
    end_quiz=check(q_no,4)
    if end_quiz and choice==question_list[4].answer:
        return redirect('result')
    que= question_list[q_no]
    
    
    last_que=check(q_no,3)   
    if choice==que.answer:
        q_no+=1
        que=question_list[q_no]
    elif choice is None:
        pass
    else:
        li.append(1)
    
    
    return render(request,'quiz.html',{'que':que,'no':q_no,'last_que':last_que})

    

def result(request):
    restart=request.GET.get('restart')
    if restart=="restart":
        li.clear()
        return redirect('home')
        
        
        
    attempt=int(len(li))
    if attempt>=3:
        result=f"Bad!!! You need more practice, you choose {attempt} wrong answer"
    elif 0 < attempt <= 2:
        result=f"Good!!! You need some more practice, you choose {attempt} wrong answer"
    elif attempt==0:
        result=f"Excellent!!! You choose {attempt} wrong answer"
        
        
    return render(request,'result.html',{'result':result})

