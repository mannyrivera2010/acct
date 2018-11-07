# Simple Account System 
This System is based on double entry accounting 

## Ideas
* User - a user of the system, a user can belong to more than 1 group
* Group - a collection of users that can see a set of projects
* Project - a collection of accounts
* Account - a collection of transactions
* Transaction - an entry that has the date, description, and amount

### Model
* There can be many users in the system  
* Each user can only belong to one group
* There can be many projects per group and only belong to one group
* There can be many accounts per project and only belong to one project, projects should not go between more than one group




https://dba.stackexchange.com/questions/102370/double-entry-bookkeeping-database-design
