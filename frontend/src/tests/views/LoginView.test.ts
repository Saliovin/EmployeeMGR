import LoginView from '@/views/LoginView.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('login', () => {
    it('base', () => {
        const login = mount(LoginView)
        expect(login.element).toMatchSnapshot()
    })
})