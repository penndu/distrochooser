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
    <div>
      <HTMLWelcome v-if="props.widget.template == 'welcomeHTML'"/>
      <HTMLLanguage v-if="props.widget.template == 'languageHTML'"/>
    </div>
</template>
<script setup lang="ts">
import type {HTMLWidget } from '../../sdk';
import HTMLWelcome from "../widgets/html/HTMLWelcome.vue";
import HTMLLanguage from './html/HTMLLanguage.vue';


// TODO: Naming for "templates" and documentation
// TODO: Mapping for child components
interface WidgetProps {
  widget: HTMLWidget;
}

const props = defineProps<WidgetProps>();

</script>