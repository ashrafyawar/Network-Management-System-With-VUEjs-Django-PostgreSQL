<template>
  <div class="content">
    <Navbar></Navbar>
    <br><br><br><br><br><br>
    <form class="container" id="myFrom">
      <label>Name</label>
      <input 
        type="text" 
        v-model="name"
        name="name"
        placeholder="Your Name"
      >
      <label>Email</label>
      <input 
        type="email" 
        v-model="email"
        name="email"
        placeholder="Your Email"
        >
      <label>Message</label>
      <textarea 
        name="message"
        v-model="message"
        cols="30" rows="5"
        placeholder="Message">
      </textarea>
      <input class="submit-button" @click="sendEmail($event)" type="submit" value="Book The Ticket">
    </form>
  </div>
</template>

<style scoped>
  * {box-sizing: border-box;}
  .submit-button{
    width: 25%;
  }
  .container {
    overflow: hidden;
    display: block;
    margin:auto;
    text-align: center;
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
    width: 50%;
  }

  label {
    float: left;
  }

  input[type=text], [type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical;
  }

  input[type=submit] {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  input[type=submit]:hover {
    background-color: #45a049;
  }
</style>

<script>
  import Navbar from '../components/Navbar.vue'
  import axios from 'axios'

  export default {
      name:'TechSupportView',
      components:{
        Navbar,
      },
      data:function(){// data to store for component
          return{
            name:"",
            email:"",
            message:"",
          }
      },
      methods:{// methods to call for a component
        sendEmail(e) {
        if (this.name != "" && this.email != "" && this.message !="") { // form demo request
          const demoInfo = {
          Name:this.name,
          Email:this.email,
          Message:this.message
          }
          axios.post('/postdemorequest',demoInfo).then(response =>{
            console.log(response);
          })
          .catch(error =>{
            console.log(error)
          })
          alert("We Recieved Your DEMO Request And Will Get Back To You Soon :)")
          this.$router.push({path:"/"})
        }else {
          alert("Fill In The Name,Email And Message Fields !!!")
        }
    },
      },
      created: function(){ // constructor, run when the page is loaded.
      }
  }
</script>