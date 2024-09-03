import Modal from '@/components/Modal.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('modal', () => {
    it('base', () => {
        const modal = mount(Modal, {
            props: {
                title: 'test',
            }
        })
        expect(modal.element).toMatchSnapshot()
    })
})