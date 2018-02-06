# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:04:41 2018

@author: user2
"""

from flask import Flask, render_template, request
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('input.html')

@app.route('/submit', methods=['POST'])
def sort():

    number1 =  int(request.form['number1'])
    number2 =  int(request.form['number2'])
    number3 =  int(request.form['number3'])
    number4 =  int(request.form['number4'])
    number5 =  int(request.form['number5'])
    mainArray = [number1,number2,number3,number4,number5]
    
    linearSortStartTime = time.time()
    
    SortedLinearArr = LinearSort(list(mainArray))

    linearSortEndTime = time.time()
    
    #A = A_backup
    InsertionSortStartTime = time.time()
    InsertionSort(list(mainArray))
  #  print(SortedInsertionArr)
    
    InsertionSortEndTime = time.time()
    
    BubbleSortStartTime = time.time()
    bubbleSort(list(mainArray))
  #  print(SortedInsertionArr)
    
    BubbleSortEndTime = time.time()
    #print(linearSortEndTime)
    return render_template('output.html', numbers=SortedLinearArr, linearSortStartTime=linearSortStartTime, linearSortEndTime=linearSortEndTime, InsertionSortStartTime=InsertionSortStartTime,InsertionSortEndTime=InsertionSortEndTime,BubbleSortStartTime=BubbleSortStartTime,BubbleSortEndTime=BubbleSortEndTime)


def LinearSort(A):

    for i in range(len(A)):
        min_idx = i
        
        for j in range(i+1, len(A)):
            
            if A[min_idx] > A[j]:
                min_idx = j
                
        A[i], A[min_idx] = A[min_idx],A[i]
        
    return A


def InsertionSort(A):

    for i in range(1, len(A)):
 
        key = A[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
    return A

def bubbleSort(arr):

    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc')