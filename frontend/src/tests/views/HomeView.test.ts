import HomeView from '@/views/HomeView.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('home', () => {
    it('base', () => {
        const modal = mount(HomeView)
        expect(modal).toMatchSnapshot()
    })
})