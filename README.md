
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
          


          
          
          

          
