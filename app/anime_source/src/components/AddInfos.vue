<template
  ><main class="profile-page" style="weight: 80%;" v-if="id != null">
    <section class="relative py-16">
      <div class="container mx-auto px-4">
        <h3
          class="text-xl font-bold block uppercase tracking-wide text-yellow-500"
        >
          More Information:
        </h3>
        <div>
          <div
            class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-5"
          >
            <template>
              <!--Card 1-->
              <div class="rounded overflow-hidden shadow-lg">
                <div
                  class="bg-white mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
                >
                  <div class="sm:flex sm:items-center px-6 py-4">
                    <img
                      class="block h-16 sm:h-24 rounded-full mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                      src="https://avatars0.githubusercontent.com/u/1006420?s=460&v=4"
                      alt=""
                    />
                    <div class="text-center sm:text-left sm:flex-grow">
                      <div class="mb-4">
                        <p class="text-xl leading-tight">Jerrie Pelser</p>
                        <p class="text-sm leading-tight text-grey-dark">
                          Freelance software developer and blogger
                        </p>
                      </div>
                      <div>
                        <button
                          class="text-xs font-semibold rounded-full px-4 py-1 leading-normal bg-white border border-purple text-purple hover:bg-purple hover:text-white"
                        >
                          Message
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="rounded overflow-hidden shadow-lg">
                <div
                  class="bg-white mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
                >
                  <div class="sm:flex sm:items-center px-6 py-4">
                    <img
                      class="block h-16 sm:h-24 rounded-full mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                      src="https://avatars0.githubusercontent.com/u/1006420?s=460&v=4"
                      alt=""
                    />
                    <div class="text-center sm:text-left sm:flex-grow">
                      <div class="mb-4">
                        <p class="text-xl leading-tight">Jerrie Pelser</p>
                        <p class="text-sm leading-tight text-grey-dark">
                          Freelance software developer and blogger
                        </p>
                      </div>
                      <div>
                        <button
                          class="text-xs font-semibold rounded-full px-4 py-1 leading-normal bg-white border border-purple text-purple hover:bg-purple hover:text-white"
                        >
                          Message
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="rounded overflow-hidden shadow-lg">
                <div
                  class="bg-white mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
                >
                  <div class="sm:flex sm:items-center px-6 py-4">
                    <img
                      class="block h-16 sm:h-24 rounded-full mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
                      src="https://avatars0.githubusercontent.com/u/1006420?s=460&v=4"
                      alt=""
                    />
                    <div class="text-center sm:text-left sm:flex-grow">
                      <div class="mb-4">
                        <p class="text-xl leading-tight">Jerrie Pelser</p>
                        <p class="text-sm leading-tight text-grey-dark">
                          Freelance software developer and blogger
                        </p>
                      </div>
                      <div>
                        <button
                          class="text-xs font-semibold rounded-full px-4 py-1 leading-normal bg-white border border-purple text-purple hover:bg-purple hover:text-white"
                        >
                          Message
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
<script>
export default {
  name: "AddInfos",
  props: {
    id: String,
  },
  data() {
    return {
      producers: null,
      licencer: null,
      studios: null,
    };
  },
};
</script>
