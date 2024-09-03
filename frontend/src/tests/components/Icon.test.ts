import Icon from '@/components/Icon.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('icon', () => {
    it('base', () => {
        const card = mount(Icon, {
            props: {
                icon: 'x',
                size: 'lg'
            }
        })
        expect(card.element).toMatchSnapshot()
    })
})