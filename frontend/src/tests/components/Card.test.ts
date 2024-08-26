import Card from '@/components/Card.vue'
import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'

describe('card', () => {
    it('base', () => {
        const card = mount(Card, {
            props: {
                first_name: 'test',
                last_name: 'testing'
            }
        })
        expect(card).toMatchSnapshot()
    })
})