<template>
  <div>
    <Navbar></Navbar>
    <br><br><br><br><br><br><br><br>
    <form>
        <div class="container register-form">
            <div class="form" method="post">
              <div class="note">
              <p><b>SUPER USER LOGIN</b></p>
              </div>
              <div class="form-content">
                <div class="row">
                    <div class="col-md-6">
                      <div class="form-group" aria-placeholder="Username">
                          <input v-model="userName" type="text" placeholder="Username" class="form-control">
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group">
                          <input v-model="password" type="text" placeholder="Password" class="form-control">
                      </div>
                    </div>
                </div>
                <button type="submit" class="btnSubmit" @click="loginClick($event)">Login</button>
                <div class="text-center">Want New Access? <RouterLink to="/signup">Signup Here</RouterLink></div>
              </div>
            </div>
        </div>
    </form>
  </div>
</template>

<script>

  import Navbar from '../components/Navbar.vue'
  import axios from 'axios'

  export default{
    name:'LoginView',
    components:{
      Navbar
    },
    data:function(){
        return{
        userExists:false,
        userName:"",
        password:"",
        usersList:[],
        }
    },
    methods:{

        loginClick(event){
          if (this.userName != "" && this.password != "") { // if sign up info is not null
            for (let index = 0; index < this.usersList.length; index++)  {
              console.log(this.usersList[index])
              if (this.userName == this.usersList[index].AdminName && this.password == this.usersList[index].AdminPassword) {
                  this.userExists = true
                  break
              }
            }

            if (this.userExists) {// if user exists in the system
                this.$router.push("/admindashboardpage")
            }else{
              alert("Wrong UserName Or Password !!!")
            }
          }else if(this.userName != "" && this.password == ""){
            alert("Fill In The Password Field !!!")
          }else if(this.userName == "" && this.password != ""){
            alert("Fill In The Username Field !!!")
          }else {
            alert("Fill In The UserName And Password Fields !!!")
          }
        },

        getUserList(){
            axios.get('/authenticate-user').then(response =>{
              this.usersList = response.data;

            })
            .catch(error =>{
              console.log(error)
            })
        }
    },
    created: function(){
      this.getUserList()
    }
  }

</script>

<style scoped>
  .form{
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  .bs-example {
    margin: 0px;

  }
  .navbar-brand {
    font-size: 20px;
    font-family: sans-serif;

  }
  body {
  color: #aa082e;
  background-color: #b6bde7;
  font-family: 'Roboto', sans-serif;
  }

  .note {
    text-align: center;
    height: 80px;
    background: -webkit-linear-gradient(left, #5f5f5f, #020102);
    color: #fff;
    font-weight: bold;
    line-height: 80px;
  }

  .form-content {
    padding: 5%;
    border: 1px solid #ced4da;
    margin-bottom: 2%;
  }

  .form-control {
    border-radius: 1.5rem;
  }

  .btnSubmit {
    border: none;
    border-radius: 1.5rem;
    padding: 1%;
    width: 20%;
    cursor: pointer;
    background: #941021;
    color: #fff;
  }
</style>