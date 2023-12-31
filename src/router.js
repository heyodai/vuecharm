import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '/home',
        name: 'Home',
        component: () => import(/* webpackChunkName: "Home" */ '../views/Home.vue')
    },
    {
        path: '/about',
        name: 'About',
        component: () => import(/* webpackChunkName: "About" */ '../views/About.vue')
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;