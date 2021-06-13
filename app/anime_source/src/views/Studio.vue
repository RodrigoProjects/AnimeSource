<template>
  <div>
    <main class="profile-page">
      <section class="relative block" style="height: 400px;">
        <div
          class="absolute top-0 w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://i.redd.it/de38p8tsp2t21.png?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=2710&amp;q=80');
          "
        ></div>
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
              class="text-gray-300 fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </section>
      <section class="relative py-16 bg-gray-300">
        <div class="container mx-auto px-4">
          <div
            class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64"
          >
            <div class="px-6">
              <div class="flex flex-wrap justify-center">
                <div
                  class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center"
                >
                  <div class="relative">
                    <img
                      alt="..."
                      :src="photo"
                      class="shadow-xl rounded-xl h-auto align-middle border-none -m-16 lg:-ml-16"
                      style="max-width: 300px;"
                    />
                  </div>
                </div>
                <div
                  class="w-full px-4 lg:order-2 lg:text-right lg:self-center"
                >
                  <div class="py-6 px-3 mt-32 sm:mt-0"></div>
                </div>
                <br /><br />
                <br /><br />
                <div class="text-center mt-12 lg:order-3">
                  <h3
                    class="text-4xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
                  >
                    {{ studio.nome }}
                  </h3>
                </div>
                <div class="w-full px-4 lg:order-3">
                  <div class="flex justify-center py-4 lg:pt-4 pt-8">
                    <div class="mr-4 p-3 text-center">
                      <span
                        class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                        >{{ total }}</span
                      ><span class="text-sm text-gray-500">Animes</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-10 py-10 border-t border-gray-300 text-center">
                <div class="flex flex-wrap justify-center">
                  <div class="w-full lg:w-9/12 px-4">
                    <p class="mb-4 text-lg leading-relaxed text-gray-800">
                      An artist of considerable range, Jenna the name taken by
                      Melbourne-raised, Brooklyn-based Nick Murphy writes,
                      performs and records all of his own music, giving it a
                      warm, intimate feel with a solid groove structure. An
                      artist of considerable range.
                    </p>
                    <hr />
                    <br />
                    <h3
                      class="text-xl font-bold block uppercase tracking-wide text-yellow-500"
                    >
                      Anime List:
                    </h3>

                    <div>
                      <div
                        class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5"
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
                                Lorem ipsum dolor sit amet, consectetur
                                adipisicing elit. Voluptatibus quia, nulla!
                                Maiores et perferendis eaque, exercitationem
                                praesentium nihil.
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
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
var gdb = require("../utils/graphdb");
var axios = require("axios");
import VueTailwindPagination from "@ocrv/vue-tailwind-pagination";
export default {
  components: {
    VueTailwindPagination,
  },
  data() {
    return {
      studio: [],
      currentPage: 1,
      perPage: 3,
      animes: [],
      total: null,
      title: this.animes,
      photo: null,
    };
  },

  created() {
    var query =
      `
    select ?nome where {
        :studio_` +
      this.$route.params.id +
      ` :name ?nome.
    }
    `;
    gdb
      .fetchOntobud(query)
      .then(async (response) => {
        this.studio = { nome: response.data.results.bindings[0].nome.value };
        var name = this.studio.nome.replace(" ", "+");
        const g = axios
          .get(
            "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
              name +
              "+studio+logo"
          )
          .then((dat) => {
            this.photo = dat.data.items[0].link;
          })
          .catch((e) => {
            console.log("Erro no get studios " + e);
          });
        await Promise.resolve(g);
      })

      .catch((e) => {
        console.log("Erro no get studios " + e);
      });
    this.list(1);
  },

  methods: {
    list: function (currentPage) {
      this.currentPage = currentPage;
      var queryA =
        `select * where {
                ?p ?d :studio_` +
        this.$route.params.id +
        `;
              :episodes ?ep;
              :title ?tit;
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
            const g = axios
              .get(
                "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
                  nome +
                  "+cover"
              )
              .then((dat) => {
                //console.log(dat);

                this.animes.push({
                  id: o.p.value.split("#")[1].split("_")[1],
                  nome: o.tit.value,
                  status: o.stat.value,
                  eps: o.ep.value,
                  photo: dat.data.items[0].link,
                  score: o.pop.value,
                });
              })
              .catch((e) => {
                console.log("Erro no get animes " + e);
              });
            await Promise.resolve(g);
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

<style></style>
