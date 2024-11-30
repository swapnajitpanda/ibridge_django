# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Activity(models.Model):
#     player_id = models.FloatField(blank=True, null=True)
#     device_id = models.FloatField(blank=True, null=True)
#     event_date = models.DateField(blank=True, null=True)
#     games_played = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'activity'


# class Awards(models.Model):
#     awardid = models.BigIntegerField(primary_key=True)
#     awardname = models.CharField(max_length=50, blank=True, null=True)
#     year = models.BigIntegerField(blank=True, null=True)
#     winnerid = models.BigIntegerField(blank=True, null=True)
#     category = models.CharField(max_length=50, blank=True, null=True)
#     winnername = models.CharField(max_length=100, blank=True, null=True)
#     winneroccupation = models.CharField(max_length=50, blank=True, null=True)
#     winnercountry = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'awards'


# class Bank(models.Model):
#     bank_id = models.CharField(max_length=20, blank=True, null=True)
#     account_id = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bank'


# class BankErrorRecords(models.Model):
#     seq_no = models.FloatField(blank=True, null=True)
#     record = models.CharField(max_length=30, blank=True, null=True)
#     reason = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bank_error_records'


# class Books(models.Model):
#     book_id = models.FloatField(primary_key=True)
#     title = models.CharField(max_length=100, blank=True, null=True)
#     author = models.CharField(max_length=100, blank=True, null=True)
#     genre = models.CharField(max_length=50, blank=True, null=True)
#     quantity_available = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'books'


# class Branch(models.Model):
#     branch_id = models.BigIntegerField(blank=True, null=True)
#     branch_name = models.TextField(blank=True, null=True)
#     city_id = models.BigIntegerField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     phone_number = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'branch'


# class Chethan(models.Model):
#     id = models.FloatField(blank=True, null=True)
#     name = models.CharField(max_length=10, blank=True, null=True)
#     phone_number = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'chethan'


# class Cinema(models.Model):
#     cinema_id = models.FloatField(primary_key=True)
#     free = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'cinema'


# class City(models.Model):
#     city_id = models.IntegerField(primary_key=True)
#     city_name = models.CharField(max_length=20, blank=True, null=True)
#     city_population = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'city'


# class ClickstreamData(models.Model):
#     id = models.FloatField(primary_key=True)
#     user_id = models.CharField(max_length=50, blank=True, null=True)
#     page = models.CharField(max_length=100, blank=True, null=True)
#     event = models.CharField(max_length=50, blank=True, null=True)
#     timestamp = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'clickstream_data'


# class Customer1(models.Model):
#     firstname = models.CharField(max_length=26, blank=True, null=True)
#     customerid = models.BigIntegerField(blank=True, null=True)
#     lastname = models.CharField(max_length=26, blank=True, null=True)
#     email = models.CharField(max_length=26, blank=True, null=True)
#     phone = models.CharField(max_length=26, blank=True, null=True)
#     address = models.CharField(max_length=26, blank=True, null=True)
#     city = models.CharField(max_length=26, blank=True, null=True)
#     state = models.CharField(max_length=26, blank=True, null=True)
#     zipcode = models.BigIntegerField(blank=True, null=True)
#     country = models.CharField(max_length=26, blank=True, null=True)
#     registrationdate = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'customer_1'


# class CustomerProduct(models.Model):
#     cust_id = models.CharField(max_length=3, blank=True, null=True)
#     prod_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'customer_product'


# class Customermaster(models.Model):
#     customerid = models.BigIntegerField(primary_key=True)
#     customername = models.CharField(max_length=100, blank=True, null=True)
#     contactnumber = models.CharField(max_length=15, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'customermaster'


# class Customers(models.Model):
#     cust_id = models.BigIntegerField(primary_key=True)
#     c_last_name = models.CharField(max_length=25)
#     c_first_name = models.CharField(max_length=25)
#     c_email = models.CharField(unique=True, max_length=100)
#     phone_number = models.CharField(max_length=10, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'customers'


# class DataConfig(models.Model):
#     table_id = models.FloatField(blank=True, null=True)
#     table_name = models.CharField(max_length=50, blank=True, null=True)
#     delete_from = models.DateField(blank=True, null=True)
#     delete_to = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'data_config'


# class Dates(models.Model):
#     c_name = models.CharField(max_length=20, blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'dates'


# class Department(models.Model):
#     department_id = models.FloatField(primary_key=True)
#     department_name = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'department'


# class Departments(models.Model):
#     department_id = models.BigIntegerField(primary_key=True)
#     department_name = models.CharField(max_length=100, blank=True, null=True)
#     location = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'departments'


# class Dept(models.Model):
#     deptno = models.BigIntegerField(blank=True, null=True)
#     dname = models.CharField(max_length=14, blank=True, null=True)
#     loc = models.CharField(max_length=13, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'dept'


# class Dept1(models.Model):
#     dept_id = models.FloatField(primary_key=True)
#     depart_name = models.CharField(max_length=25, blank=True, null=True)
#     dept_loc = models.CharField(max_length=25, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'dept1'


# class Doctor(models.Model):
#     doc_id = models.CharField(primary_key=True, max_length=4)
#     fname = models.CharField(max_length=20, blank=True, null=True)
#     lname = models.CharField(max_length=20, blank=True, null=True)
#     specialty = models.CharField(max_length=20, blank=True, null=True)
#     phone = models.IntegerField(blank=True, null=True)
#     fee = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'doctor'


# class Emp(models.Model):
#     empno = models.BigIntegerField(blank=True, null=True)
#     ename = models.CharField(max_length=10, blank=True, null=True)
#     job = models.CharField(max_length=9, blank=True, null=True)
#     mgr = models.BigIntegerField(blank=True, null=True)
#     hiredate = models.DateField(blank=True, null=True)
#     sal = models.BigIntegerField(blank=True, null=True)
#     comm = models.BigIntegerField(blank=True, null=True)
#     deptno = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'emp'


# class Emp1(models.Model):
#     emp_id = models.FloatField(primary_key=True)
#     emp_name = models.CharField(max_length=25, blank=True, null=True)
#     emp_salary = models.CharField(max_length=25, blank=True, null=True)
#     dept = models.ForeignKey(Dept1, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'emp1'


# class Emp2(models.Model):
#     empno = models.IntegerField()
#     ename = models.CharField(max_length=10, blank=True, null=True)
#     job = models.CharField(max_length=9, blank=True, null=True)
#     mgr = models.IntegerField(blank=True, null=True)
#     hiredate = models.DateField(blank=True, null=True)
#     sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
#     comm = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
#     deptno = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'emp2'


# class Emp3(models.Model):
#     employee_id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=20, blank=True, null=True)
#     last_name = models.CharField(max_length=25)
#     email = models.CharField(max_length=25)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     hire_date = models.DateField()
#     job_id = models.CharField(max_length=10)
#     salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
#     commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
#     manager_id = models.IntegerField(blank=True, null=True)
#     department_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'emp3'


# class Employee1(models.Model):
#     employee_id = models.BigIntegerField(primary_key=True)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     department_id = models.BigIntegerField(blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee1'


# class Employee15072024(models.Model):
#     employee_id = models.FloatField(primary_key=True)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     salary = models.FloatField(blank=True, null=True)
#     department_id = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee15_07_2024'


# class Employee2(models.Model):
#     eid = models.IntegerField(blank=True, null=True)
#     ename = models.CharField(max_length=15)
#     sal = models.IntegerField()
#     dept = models.CharField(max_length=15)
#     doj = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee2'


# class Employee4(models.Model):
#     employee_id = models.BigIntegerField(primary_key=True)
#     employee_name = models.CharField(max_length=100, blank=True, null=True)
#     department = models.CharField(max_length=100, blank=True, null=True)
#     age = models.BigIntegerField(blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee4'


# class Employee(models.Model):
#     employee_id = models.FloatField(primary_key=True)
#     employee_name = models.CharField(max_length=100, blank=True, null=True)
#     department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_'


# class Employees(models.Model):
#     employee_id = models.BigIntegerField(primary_key=True)
#     employee_name = models.CharField(max_length=50, blank=True, null=True)
#     supervisor_id = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employees'


# class Employees1(models.Model):
#     employee_id = models.BigIntegerField(primary_key=True)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employees1'


# class Employees2(models.Model):
#     emp_id = models.FloatField(blank=True, null=True)
#     emp_name = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employees2'


# class Employees3(models.Model):
#     employeeid = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     departmentid = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employees3'


# class Employees4(models.Model):
#     employee_id = models.BigIntegerField(primary_key=True)
#     employee_name = models.CharField(max_length=100, blank=True, null=True)
#     department = models.CharField(max_length=100, blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employees4'


# class Events(models.Model):
#     event_id = models.FloatField(primary_key=True)
#     event_name = models.CharField(max_length=255, blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     location = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'events'


# class Hacker(models.Model):
#     hacker_id = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'hacker'


# class Input(models.Model):
#     groupf = models.CharField(max_length=10, blank=True, null=True)
#     sequence = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'input'


# class Matches(models.Model):
#     match_id = models.FloatField(primary_key=True)
#     match_date = models.DateField(blank=True, null=True)
#     game = models.CharField(max_length=100, blank=True, null=True)
#     public_tickets = models.FloatField(blank=True, null=True)
#     sponsor_tickets = models.FloatField(blank=True, null=True)
#     public_ticket_price = models.FloatField(blank=True, null=True)
#     sponsor_ticket_price = models.FloatField(blank=True, null=True)
#     sta = models.ForeignKey('Stadium', models.DO_NOTHING, blank=True, null=True)
#     home_team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
#     visiting_team = models.ForeignKey('Team', models.DO_NOTHING, related_name='matches_visiting_team_set', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'matches'


# class MyTabe(models.Model):
#     id = models.FloatField(primary_key=True)
#     name = models.CharField(max_length=30, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'my_tabe'


# class NodeTypesParent(models.Model):
#     node = models.IntegerField(blank=True, null=True)
#     parent = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'node_types_parent'


# class Nodes(models.Model):
#     n = models.IntegerField(blank=True, null=True)
#     p = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodes'


# class NotNull(models.Model):
#     customer_id = models.IntegerField()
#     customer_name = models.CharField(max_length=10)
#     customer_dob = models.DateField(blank=True, null=True)
#     customer_phno = models.IntegerField(blank=True, null=True)
#     customer_email = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'not_null'


# class Occupations(models.Model):
#     names = models.CharField(max_length=30, blank=True, null=True)
#     occupation = models.CharField(max_length=30, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'occupations'


# class Offices(models.Model):
#     officecode = models.CharField(primary_key=True, max_length=10)
#     city = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     addressline1 = models.CharField(max_length=50)
#     addressline2 = models.CharField(max_length=50, blank=True, null=True)
#     state = models.CharField(max_length=50, blank=True, null=True)
#     country = models.CharField(max_length=50)
#     postalcode = models.CharField(max_length=15)
#     territory = models.CharField(max_length=10)

#     class Meta:
#         managed = False
#         db_table = 'offices'


# class Orders(models.Model):
#     order_id = models.FloatField(primary_key=True)
#     book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
#     member_id = models.FloatField(blank=True, null=True)
#     order_date = models.DateField(blank=True, null=True)
#     return_date = models.DateField(blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'orders'


# class OrdersVj(models.Model):
#     order_id = models.FloatField(primary_key=True)
#     cust = models.ForeignKey(Customers, models.DO_NOTHING)
#     order_date = models.DateField()
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'orders_vj'


# class Overlap(models.Model):
#     userid = models.CharField(max_length=5, blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'overlap'


# class Ports(models.Model):
#     port_id = models.FloatField(primary_key=True)
#     port_name = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'ports'


# class Product(models.Model):
#     p_id = models.IntegerField(blank=True, null=True)
#     p_name = models.CharField(max_length=20, blank=True, null=True)
#     p_family = models.CharField(max_length=20, blank=True, null=True)
#     price = models.IntegerField(blank=True, null=True)
#     cost = models.IntegerField(blank=True, null=True)
#     launch_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'product'


# class ProductCustomer(models.Model):
#     prod_id = models.IntegerField(blank=True, null=True)
#     product_name = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'product_customer'


# class Productmaster(models.Model):
#     productid = models.BigIntegerField(primary_key=True)
#     productname = models.CharField(max_length=100, blank=True, null=True)
#     category = models.CharField(max_length=50, blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     stockquantity = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'productmaster'


# class Resorts(models.Model):
#     resort_id = models.IntegerField(blank=True, null=True)
#     resort_name = models.CharField(max_length=20, blank=True, null=True)
#     country_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resorts'


# class Sales(models.Model):
#     sale_date = models.DateField(blank=True, null=True)
#     amount = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sales'


# class Sales1(models.Model):
#     product_id = models.FloatField(blank=True, null=True)
#     sales_date = models.DateField(blank=True, null=True)
#     revenue = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sales1'


# class Shipments(models.Model):
#     shipment_id = models.FloatField(primary_key=True)
#     origin_port = models.ForeignKey(Ports, models.DO_NOTHING, blank=True, null=True)
#     destination_port = models.ForeignKey(Ports, models.DO_NOTHING, related_name='shipments_destination_port_set', blank=True, null=True)
#     vessel = models.ForeignKey('Vessels', models.DO_NOTHING, blank=True, null=True)
#     transit_time = models.FloatField(blank=True, null=True)
#     shipment_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'shipments'


# class Stadium(models.Model):
#     sta_id = models.FloatField(primary_key=True)
#     sta_code = models.CharField(max_length=10, blank=True, null=True)
#     sta_name = models.CharField(max_length=100)
#     sta_capacity = models.FloatField(blank=True, null=True)
#     sta_type = models.CharField(max_length=50, blank=True, null=True)
#     sta_city = models.CharField(max_length=50, blank=True, null=True)
#     sta_opened_date = models.DateField(blank=True, null=True)
#     sta_status = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'stadium'


# class Student(models.Model):
#     id = models.FloatField(primary_key=True)
#     name = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'student'


# class Students(models.Model):
#     id = models.FloatField(primary_key=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     score = models.IntegerField(blank=True, null=True)
#     enrollment_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'students'


# class Tablea(models.Model):
#     a = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tablea'


# class Tableb(models.Model):
#     b = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tableb'


# class TargetAccount(models.Model):
#     bank_id = models.CharField(max_length=10, blank=True, null=True)
#     account_type = models.CharField(max_length=10, blank=True, null=True)
#     account_no = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'target_account'


# class Team(models.Model):
#     team_id = models.FloatField(primary_key=True)
#     team_nm = models.CharField(max_length=100)
#     game = models.CharField(max_length=100, blank=True, null=True)
#     operational_from = models.DateField(blank=True, null=True)
#     manager = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'team'


# class TeamOwners(models.Model):
#     own_id = models.FloatField(primary_key=True)
#     own_name = models.CharField(max_length=100)
#     team = models.ForeignKey(Team, models.DO_NOTHING, blank=True, null=True)
#     percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'team_owners'


# # class TimeSheet(models.Model):
# #     employeeid = models.FloatField(blank=True, null=True)
# #     hoursworked = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
# #     date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.

# #     class Meta:
# #         managed = False
# #         db_table = 'time_sheet'


# class Timesheet(models.Model):
#     timesheet_id = models.FloatField(primary_key=True)
#     employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
#     hours_worked = models.FloatField(blank=True, null=True)
#     date_worked = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'timesheet'


# class Transaction(models.Model):
#     transactionid = models.BigIntegerField(primary_key=True)
#     transactiondate = models.DateField(blank=True, null=True)
#     customerid = models.ForeignKey(Customermaster, models.DO_NOTHING, db_column='customerid', blank=True, null=True)
#     productid = models.ForeignKey(Productmaster, models.DO_NOTHING, db_column='productid', blank=True, null=True)
#     quantity = models.BigIntegerField(blank=True, null=True)
#     totalamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'transaction'


# class Transactions(models.Model):
#     transaction_id = models.FloatField(primary_key=True)
#     customer_id = models.FloatField(blank=True, null=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     timestamp = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'transactions'


# class Uniques(models.Model):
#     customer_id = models.IntegerField(unique=True, blank=True, null=True)
#     customer_name = models.CharField(max_length=10, blank=True, null=True)
#     customer_dob = models.DateField(blank=True, null=True)
#     customer_phno = models.IntegerField(blank=True, null=True)
#     customer_email = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'uniques'


class UserActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    recordeddate = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    inserted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_activity'


# class Users(models.Model):
#     id = models.BigIntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     username = models.TextField(blank=True, null=True)
#     email = models.TextField(blank=True, null=True)
#     street = models.TextField(blank=True, null=True)
#     suite = models.TextField(blank=True, null=True)
#     city = models.TextField(blank=True, null=True)
#     zipcode = models.TextField(blank=True, null=True)
#     geo_lat = models.TextField(blank=True, null=True)
#     geo_lng = models.TextField(blank=True, null=True)
#     phone = models.TextField(blank=True, null=True)
#     website = models.TextField(blank=True, null=True)
#     company_name = models.TextField(blank=True, null=True)
#     catch_phrase = models.TextField(blank=True, null=True)
#     bs = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'users'


# class Vessels(models.Model):
#     vessel_id = models.FloatField(primary_key=True)
#     vessel_name = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'vessels'
