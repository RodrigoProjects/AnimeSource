<template>
  <div>
    <div
      class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5"
    >
      <template v-for="item in studios" :key="item">
        <!--Card 1-->
        <div class="rounded overflow-hidden shadow-lg">
          <img class="w-full" :src="item.photo" alt="Mountain" />
          <div class="px-6 py-4">
            <router-link
              :to="{ name: 'Studio', params: { id: item.id } }"
              class="font-bold text-xl mb-2"
              >{{ item.nome }}</router-link
            >
            <p class="text-gray-700 text-base">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Voluptatibus quia, nulla! Maiores et perferendis eaque,
              exercitationem praesentium nihil.
            </p>
          </div>
          <div class="px-6 pt-4 pb-2">
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#photography</span
            >
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#travel</span
            >
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
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
</template>

<script>
var gdb = require("../utils/graphdb");
import VueTailwindPagination from "@ocrv/vue-tailwind-pagination";
//const axios = require("axios");

export default {
  components: {
    VueTailwindPagination,
  },
  data() {
    return {
      studios: [],
      currentPage: 1,
      perPage: 9,
      title: this.studios,
      total: null,
    };
  },

  created() {
    this.list(1);
  },

  methods: {
    list: function (currentPage) {
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
        .then((response) => {
          this.total = response.data.results.bindings.length;

          var i = 0;
          while (i < 9) {
            var d =
              response.data.results.bindings[
                (this.currentPage - 1) * this.perPage + i
              ];

            //var nome = d.nome.value.replace(" ", "+");
            //axios
            //  .get(
            //    "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
            //      nome +
            //      "+studio+logo"
            //  )
            //  .then((dat) => {
            //    console.log(dat);

            this.studios.push({
              id: d.studio.value.split("#")[1].split("_")[1],
              NAnimes: d.NAnimes.value,
              nome: d.nome.value,
            });
            i = i + 1;
            // });
          }
          console.log(this.studios);
          //})
          //.catch((e) => {
          //  console.log("Erro no get studios " + e);
          //});
        })
        .catch((e) => {
          console.log("Erro no get studios " + e);
        });
    },
  },
};
</script>

<style></style>
