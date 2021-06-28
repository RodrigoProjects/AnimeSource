<template>
  <main class="profile-page" style="weight: 80%;" v-if="total != null">
    <section class="relative py-16">
      <div class="container mx-auto px-4">
        <h3
          class="text-xl font-bold block uppercase tracking-wide text-yellow-500"
        >
          Anime List:
        </h3>

        <div>
          <div
            class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-5"
          >
            <template v-for="item in animes" :key="item">
              <!--Card 1-->
              <div class="rounded overflow-hidden shadow-lg">
                <img
                  class="object-contain h-96 w-full"
                  :src="item.photo"
                  alt="Mountain"
                />
                <div class="px-6 py-4">
                  <router-link
                    :to="{
                      name: 'Anime',
                      params: { id: item.id },
                    }"
                    class="font-bold text-xl mb-2"
                    >{{ item.nome }}</router-link
                  >
                  <p class="text-gray-700 text-base">
                    {{ item.background }}
                  </p>
                </div>
                <div class="px-6 pt-4 pb-2">
                  <span
                    class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                    >{{ item.eps }} Episodes</span
                  >
                  <span
                    class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                    >#{{ item.status }}</span
                  >
                  <span
                    class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
                    >#Score {{ item.score }}</span
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
      </div>
    </section>
  </main>
</template>

<script>
var axios = require("axios");
import VueTailwindPagination from "../components/Pagination.vue";
var gdb = require("../utils/graphdb");
export default {
  components: {
    VueTailwindPagination,
  },
  props: {
    tipe: String,
    id: String,
  },
  data() {
    return {
      currentPage: 1,
      perPage: 3,
      animes: [],
      total: null,
      title: this.animes,
    };
  },
  created() {
    this.list(1);
  },

  methods: {
    list: function (currentPage) {
      this.animes = [];
      this.currentPage = currentPage;
      var queryA =
        `select * where {
                ?p ?d :` +
        this.tipe +
        `_` +
        this.id +
        `;
              :episodes ?ep;
              :title ?tit;
              :background ?back;
              :status ?stat;
                    :score ?pop.
            } order by DESC(?pop)
            `;
      gdb
        .fetchOntobud(queryA)
        .then(async (respo) => {
          this.total = respo.data.results.bindings.length;

          var i = 0;
          while (i < 3) {
            var o =
              respo.data.results.bindings[
                (this.currentPage - 1) * this.perPage + i
              ];

            var nome = o.tit.value.replace(" ", "+");
            var pic =
              "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg";
            const g = axios
              .get(
                "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
                  nome +
                  "+cover"
              )
              .then((dat) => {
                pic = dat.data.items[1].link;
              })
              .catch((e) => {
                console.log("Erro no get animes " + e);
              });

            await Promise.resolve(g);
            this.animes.push({
              id: o.p.value.split("#")[1].split("_")[1],
              nome: o.tit.value,
              status: o.stat.value,
              background: o.back.value,
              eps: o.ep.value,
              photo: pic,
              score: o.pop.value,
            });
            i = i + 1;
          }
        })
        .catch((e) => {
          console.log("Erro no get animes " + e);
        });
    },
  },
};
</script>
