<!--
distrochooser
Copyright (C) 2014-2025 Christoph Müller  <mail@chmr.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
-->
<template>
    <ul class="dropdown-menu">
        <li v-for="(key, value, index) in Object.entries(store.session.languageCodes)">
            <a class="dropdown-item"  href="#" v-on:click.prevent="store.changeLanguage(key[0])">
                <span :class="'fi fi-' + key[0]">
                </span>
                {{ key[1] }}
            </a>
        </li>
    </ul>
</template>
<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { useSessionStore } from '../states/session';

const store = useSessionStore();

</script>