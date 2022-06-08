
Library Management

Features of the Project:
1. Admin Can:

  SignUp:
  
      a) Insert admin details in tables.
  
      b) An admin records should be unique based on email, which means duplicates records should not be able to enter in DB.
  
  Login:
  
      a) The Admin can log in based on email and password.
  
  Create an entry for Books.
  
      a) The admin can create a new entry of a book.

  Retrieve all the books.
  
      a) Retrieve all the books.

  Update a book.
  
      a) The book records should be able to update.
      
  Delete a book.
  
      a) The book record should be deleted
      
2. Student Can:

  View all the records of book
  

Backend:

    Stu app
          We need this for writing our student models 
          Student model has the first+last name ,studentID which is one-to-one field to Django' User model and password. 
          We use Django's User Model for authentication . 
          There will be 3 views: login,signup and viewbookstudent. The urls will have /< login or signup or viewbookstudent>/.
          viewbookstudent view: is used to show all the available books in library to students.
          
    Libr app
          This is our app where we will write our admin and book model. It comprises of 2 models:
          Admin - for storing admin information
          Book - for storing name , author, isbn ,category of a book
          There will be 6 views: login, signup, addbook, viewbook, update, delete. The urls will have /<login_admin or admin_signup or addbook or viewbook or edit or delete>/.
          addbook view: used to enter new book entry.
          viewbook view: used to show all avaliable book to admin.
          edit view: to update book details.
          delete view: to delete a books emtry.
          
 Screenshots:
 
          Student SignUp:
          ![](Screenshot/Screenshot%20(114))
        
          Student Login:
          ![Screenshot (115)](https://user-images.githubusercontent.com/67259410/172551749-961c8f39-3216-475c-9b95-ee6cacea5c62.png)
          
          Student View Book:
          ![Screenshot (116)](https://user-images.githubusercontent.com/67259410/172551775-1a65300b-0d45-4498-9552-458afc05a6da.png)

          
          Admin Signup:
          ![Screenshot (117)](https://user-images.githubusercontent.com/67259410/172551800-547a7186-5fdd-40b7-86b1-4885bbe04046.png)

          
          Admin Login:
          ![Screenshot (118)](https://user-images.githubusercontent.com/67259410/172551829-4313626f-fa97-4bc5-8d7c-e1a11c28f61a.png)

          
          Admin Add Books:
          ![Screenshot (121)](https://user-images.githubusercontent.com/67259410/172551983-ee5294e6-0dfc-404d-ae5a-d9b49b0cb14d.png)

          
          Admin View Books:
          ![Screenshot (119)](https://user-images.githubusercontent.com/67259410/172551850-fb5859a1-6efa-4cdc-8608-28a44e62a279.png)

          
          Admin Update Books:
          ![Screenshot (120)](https://user-images.githubusercontent.com/67259410/172551868-ac747e3b-98f7-437d-b43c-21473293c577.png)

          
          
          

          
