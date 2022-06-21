<template>
  <div class="mainclass">    
    <admin-dashboard-base-view/>
    <h1 style="padding-left: 500px">applications</h1>
  </div>
</template>

<script>
  import AdminDashboardCardView from'../components/AdminDashboardCardsView.vue'
  import AdminDashboardBaseView from'../components/AdminDashboardBaseView.vue'
  import axios from 'axios'

 export default{
    name:'AdminDashboardApplicationsView',
    components:{
      AdminDashboardCardView,
      AdminDashboardBaseView
    },
    data:function(){
        return{
          userName:"ashraf",
          password:"pass",
          deviceInfo:[]
        }
    },
    methods:{
      getAdminList(){
        axios.get('/devicelist').then(response =>{
          this.deviceInfo = response.data
          console.log(this.deviceInfo);
        })
        .catch(error =>{
          console.log(error)
        })
      }
    },
    created: function(){
      this.getAdminList()
    }
  }

</script>

<style scoped>

</style>