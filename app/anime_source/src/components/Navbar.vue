<template>
  <Disclosure as="nav" class="bg-yellow-500 shadow-lg w-full" v-slot="{ open }">
    <div class="mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="flex items-center justify-between h-16 w-full">
        <div class="flex items-center justify-between w-full">
          <div
            class="flex-shrink-0 text-white font-extrabold text-2xl font-mono"
          >
            <router-link to="/">AnimeSource</router-link>
          </div>
          <div>
            <input
              type="text"
              name="anime"
              id="anime"
              class="focus:ring-yellow-700 focus:border-yellow-600 pl-2 pr-2 sm:text-sm border-yellow-500 xl:w-120 md:w-96 lg:block hidden rounded-md"
              placeholder="Search here..."
            />
          </div>
          <div class="hidden md:block">
            <div class="flex items-baseline space-x-4">
              <template v-for="item in navigation" :key="item">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <router-link
                  :to="{ name: item }"
                  class="hover:bg-yellow-400 text-lg font-mono text-white px-3 py-2 rounded-md font-black"
                  >{{ item }}</router-link
                >
              </template>
            </div>
          </div>
        </div>
        <div class="-mr-2 flex md:hidden">
          <!-- Mobile menu button -->
          <DisclosureButton
            class="bg-yellow-600 inline-flex items-center justify-center p-2 rounded-md text-white hover:text-white hover:bg-yellow-400 focus:outline-none focus:ring-offset-2 focus:ring-offset-yellow-800 focus:ring-white"
          >
            <span class="sr-only">Open main menu</span>
            <MenuIcon
              v-if="!open"
              class="block h-6 w-6 text-white"
              aria-hidden="true"
            />
            <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
      </div>
    </div>

    <DisclosurePanel class="md:hidden">
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <template v-for="(item, itemIdx) in navigation" :key="item">
          <template v-if="itemIdx === 0">
            <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
            <a
              :href="item"
              class="bg-yellow-600 text-white hover:bg-yellow-400 block px-3 py-2 rounded-md text-base font-medium"
              >{{ item }}</a
            >
          </template>
          <a
            v-else
            :href="item"
            class="bg-yellow-600 text-white hover:bg-yellow-400 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
            >{{ item }}</a
          >
        </template>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>

<script>
import { ref } from "vue";
import { Disclosure, DisclosureButton, DisclosurePanel } from "@headlessui/vue";
import { MenuIcon, XIcon } from "@heroicons/vue/outline";

const navigation = ["Studios", "Producers"];
const profile = ["Your Profile", "Settings", "Sign out"];

export default {
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    MenuIcon,
    XIcon,
  },
  setup() {
    const open = ref(false);

    return {
      navigation,
      profile,
      open,
    };
  },
};
</script>

<style></style>
