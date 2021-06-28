import { createRouter, createWebHistory } from "vue-router";
const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
  },
  {
    path: "/anime",
    name: "Animes",
    component: () => import("@/views/Anime.vue"),
  },
  {
    path: "/anime/:id",
    name: "Anime",

    component: () => import("@/views/Anime.vue"),
  },
  {
    path: "/editor",
    name: "Editors",
    component: () => import("@/views/Editor.vue"),
  },
  {
    path: "/producers",
    name: "Producers",
    component: () => import("@/views/Producers.vue"),
  },
  {
    path: "/search/:id",
    name: "Search",
    component: () => import("@/views/Results.vue"),
  },
  {
    path: "/producers/:id",
    name: "Producer",

    component: () => import("@/views/Producer.vue"),
  },
  {
    path: "/genre/:id",
    name: "Genre",
    component: () => import("@/views/Genre.vue"),
  },
  {
    path: "/studios",
    name: "Studios",
    component: () => import("@/views/Studios.vue"),
  },
  {
    path: "/studios/:id",
    name: "Studio",
    component: () => import("@/views/Studio.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
