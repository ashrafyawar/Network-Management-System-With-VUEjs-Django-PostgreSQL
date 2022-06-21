import { createRouter, createWebHistory } from 'vue-router'
import AboutSystemView from '../views/AboutSystemView.vue'
import TechSupportView from '../views/TechSupportView.vue'
import LoginView from '../views/LoginView.vue'
import AdminDashboardView from '../views/AdminDashboardView.vue'
import AdminDashboardSitesView from '../views/AdminDashboardSitesView.vue'
import AdminDashboardEdgeClustersView from '../views/AdminDashboardEdgeClustersView.vue'
import AdminDashboardAccessPointsView from '../views/AdminDashboardAccessPointsView.vue'
import AdminDashboardDevicesView from '../views/AdminDashboardDevicesView.vue'
import AdminDashboardDeviceGroupsView from '../views/AdminDashboardDeviceGroupsView.vue'
import AdminDashboardApplicationsView from '../views/AdminDashboardApplicationsView.vue'
import AdminDashboardMicroslicingView from '../views/AdminDashboardMicroslicingView.vue'

import SignupView from '../views/SignupView.vue'

const router = createRouter({
  
  history: createWebHistory(import.meta.env.BASE_URL),
  
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },{
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },{
      path: '/admindashboardpage',
      name: 'admindashboardpage',
      component: AdminDashboardView,
    },{
      path: '/admindashboardsitespage',
      name: 'admindashboardsitespage',
      component: AdminDashboardSitesView,
    },{
      path: '/admindashboardedgeclusterspage',
      name: 'admindashboardedgeclusterspage',
      component: AdminDashboardEdgeClustersView,
    },{
      path: '/admindashboardaccesspointspage',
      name: 'admindashboardaccesspointspage',
      component: AdminDashboardAccessPointsView,
    },{
      path: '/admindashboarddevicespage',
      name: 'admindashboarddevicespage',
      component: AdminDashboardDevicesView,
    },{
      path: '/admindashboarddevicegroupspage',
      name: 'admindashboarddevicegroupspage',
      component: AdminDashboardDeviceGroupsView,
    },{
      path: '/admindashboardapplicationspage',
      name: 'admindashboardapplicationspage',
      component: AdminDashboardApplicationsView,
    },{
      path: '/admindashboardmicroslicingpage',
      name: 'admindashboardmicroslicingpage',
      component: AdminDashboardMicroslicingView,
    }
    ,{
      path: '/aboutsystempage',
      name: 'aboutsystempage',
      component: AboutSystemView,
    },{
      path: '/techsupportpage',
      name: 'techsupportpage',
      component: TechSupportView,
    }
  ]
})

export default router