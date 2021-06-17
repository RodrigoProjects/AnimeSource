<template>
  <main class="profile-page">
    <section class="relative block h-64">
      <div
        class="absolute top-0 w-full h-64 bg-center bg-cover"
        style="
          background-image: url('https://i.pinimg.com/originals/a5/67/e0/a567e0483c452fd2c3a10a029edab41d.jpg?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=1710&amp;q=40');
          opacity: 80%;
        "
      >
        <br /><br />
        <div class="font-bold text-8xl mb-2 text-yellow-100 text-center">
          Studios
        </div>
      </div>
      <div
        class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden"
        style="height: 70px;"
      >
        <svg
          class="absolute bottom-0 overflow-hidden"
          xmlns="http://www.w3.org/2000/svg"
          preserveAspectRatio="none"
          version="1.1"
          viewBox="0 0 2560 100"
          x="0"
          y="0"
        >
          <polygon
            class="text-white fill-current"
            points="2560 0 2560 100 0 100"
          ></polygon>
        </svg>
      </div>
    </section>
    <div>
      <div
        class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5"
      >
        <template v-for="item in studios" :key="item">
          <!--Card 1-->
          <div class="rounded overflow-hidden shadow-lg">
            <img
              class="object-contain h-48 w-full"
              :src="item.photo"
              alt="Mountain"
            />
            <div class="px-6 py-4">
              <router-link
                :to="{ name: 'Studio', params: { id: item.id } }"
                class="font-bold text-xl mb-2"
                >{{ item.nome }}</router-link
              >
              <p class="text-gray-700 text-base">
                {{ item.snip }}
              </p>
            </div>
            <div class="px-6 pt-4 pb-2">
              <span
                class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#photography</span
              >
              <span
                class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#travel</span
              >
              <span
                class="inline-block bg-yellow-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                >#winter</span
              >
            </div>
          </div>
        </template>
      </div>
      <VueTailwindPagination
        :current="currentPage"
        :total="total"
        :per-page="perPage"
        @page-changed="
          current = $event;
          list(current);
        "
      />
    </div>
  </main>
</template>

<script>
var gdb = require("../utils/graphdb");
import VueTailwindPagination from "../components/Pagination.vue";
const axios = require("axios");

export default {
  components: {
    VueTailwindPagination,
  },
  data() {
    return {
      studios: [],
      currentPage: 1,
      perPage: 3,
      title: this.studios,
      total: null,
    };
  },

  created() {
    this.list(1);
  },

  methods: {
    list: function (currentPage) {
      this.studios = [];
      this.currentPage = currentPage;
      var query = `
    select (count(?anime) as ?NAnimes ) ?studio ?nome  where {
        ?anime ?s :Anime;
             :hasStudio ?studio.
        ?studio :name ?nome.
    } group by ?studio ?nome
      order by DESC(?NAnimes)
    `;

      gdb
        .fetchOntobud(query)
        .then(async (response) => {
          this.total = response.data.results.bindings.length;

          var i = 0;
          while (i < 3) {
            var d =
              response.data.results.bindings[
                (this.currentPage - 1) * this.perPage + i
              ];

            var nome = d.nome.value.replace(" ", "+");
            const p = axios
              .get(
                "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
                  nome +
                  "+studio+logo"
              )
              .then((dat) => {
                console.log(dat);
                this.studios.push({
                  id: d.studio.value.split("#")[1].split("_")[1],
                  NAnimes: d.NAnimes.value,
                  nome: d.nome.value,
                  photo: dat.data.items[0].link,
                });
              })
              .catch((e) => {
                console.log("Erro no get studios " + e);
                this.studios.push({
                  id: d.studio.value.split("#")[1].split("_")[1],
                  NAnimes: d.NAnimes.value,
                  nome: d.nome.value,
                  photo:
                    "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg",
                });
              });
            await Promise.resolve(p);
            i = i + 1;
          }

          console.log(this.studios);
        })
        .catch((e) => {
          console.log("Erro no get studios " + e);
        });
    },
  },
};
</script>

<style></style>
