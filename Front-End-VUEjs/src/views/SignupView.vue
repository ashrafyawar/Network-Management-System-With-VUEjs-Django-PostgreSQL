<template>    
  <div>
    <Navbar></Navbar>
    <br><br><br><br><br><br><br><br><br>
    <form>
        <div class="container register-form">
            <div class="form" method="post">
              <div class="note">
              <p><b>SUPER USER SIGN-UP</b></p>
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
                <button type="submit" class="btnSubmit" @click="signupClick($event)">Sign Up</button>
                <div class="text-center">Already An Admin? <RouterLink to="/">Login Here</RouterLink></div>
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
    name:'SignupView',
    components:{
      Navbar
    },
    data:function(){
        return{
        submitted:false,
        userName:"",
        password:""
        }
    },
    methods:{
      signupClick(event){
        if (this.userName != "" && this.password != "") { // if sign up info is not null
          const userInfo = {
          AdminName:this.userName,
          AdminPassword:this.password
          }
          axios.post('/submitadmin',userInfo).then(response =>{
            console.log(response);
            if (response == "Added Successfully") {
              this.submitted = true;
            }
          })
          .catch(error =>{
            console.log(error)
          })
          this.$router.push({path:"/"})
        }else if(this.userName != "" && this.password == ""){
          alert("Fill In The Password Field !!!")
        }else if(this.userName == "" && this.password != ""){
          alert("Fill In The Username Field !!!")
        }else {
          alert("Fill In The Username Password Fields !!!")
        }
      }
    }
  }

</script>

<style scoped>
.form{
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);

}
.alert {
  padding: 20px;
  background-color: #04AA6D;
  color: white;
}

.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.closebtn:hover {
  color: black;
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