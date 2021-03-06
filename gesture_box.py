from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.gesture import GestureDatabase
from kivy.gesture import Gesture

gesture_strings = { 'left_to_right': 'eNq1l89y2jAQxu96EbiE0WpXf/YF6LUzPECHJh7CJAUPOG3z9l2tTExIHLsHcVgS6dNP8n6ytCz3T/vfr6tdc+5eTo351n+31iwfWjCbxWH7q1mY1smf8oXmvFmcu9PxqTnLv2SWz603y08hG5WZNmRUlPHtcX/o8rCUh/HIsO9ZZVooK8hLeJUh4MzarixZBxAuMUFezt/cjWZ9Z1fBoUuWLtGcf26/noR0Em92o/xdj/bBe+sC9XEGW58b4hy2Y6ZoUx/jNDspm2ewKf0n22niHVRhO2XjDDayg8AIJQL7abia6XwduLrpYh242unm2IlIyOAvUZ55Co7qJ0IduBqKcwx1IUZH6RLDNFv9RF+FrXbiHDvhJilpGq52IleBk9pJUAeudhLWgaufNMdPC9dwZD/tKKmjFCvR1VLiOnSvnnqoRFdT/WAq+hiinEsaA8glWPC5i4gj+j7KJTpNV1f94KpzhJhCH0M+/no6gLVy1ZVomWcsXU31sQ5cPfVcBR7U0jBYat9Zio5xoKerHgfTpUVQRwPWgauhoTf0TvNiwfpUInh2b/B3CZMtOYOujoZYia6WBh7oaK9rFC9H8xs9vtvr05ZGtTTCACe6qjcx74qejZCYIHKJMxYe1dGIA9tfCog+DpsRyQebKPRxuuqK6mj0s+D+OityJAk8l/z3p6Y5vBXwcsNKBR+jWa4ljStr1nID5G04fILp2pjMVhQpjitYFexHFclmBdrxWeR4zAoXxhVOFcjjClSF/2IWUkX6QuGzggBuu0bkQeXOFaCMyo1RGzGt+PpDopA2VWhO5WeIDkN3KxSF5pQCf1yHKwzWnFIsGdPESaOmUcqnT4ZhUWgaicuKnf04NWNR0CeMz+RU5GEcWHLKaSaw5JR5HBhvFPpgktOyzx+b/e6xkx3ObNbuxrX8qm0Wf/YP3WP+yWltlmQfpLU7Pjen7eG+0R7Qkze392/kj/Z0fHi577RXXkJJqGcQ8wMGedcQ8vGz+gc2PvoZ',

'right_to_left': 'eNq1l8tu2zoQhvd6kXhzjLlwbi/gbgvkAQ6cxEiMtolguz2nb19yJPhS1JU28sKyfw4/kvNT1Gi1/7L/8XP9ujuevh923afx2kO3eumxe3x4337bPXQ91Z/1wt3x8eF4Onx82R3r39KtvvbSrf4IecywrteGstq//9i/n1o3b93iTrfPLarrcZhBm8LP2gWp28AaEMMMXRnRXC2ozef/1s6tXRRIFSU0xNFKd3za/n2UkqNI93p/gNeBXbwQgTAxBgeaTcNz5WjLwD3hcYZDW3BAiUKh4hd00ethZySFMvWEFzSIAY8zpCC9ot+0MU/DKeG8DDztpNHOf1rKvRQELcpuzqx2hpMJhJwHmAFPO8mWgaedFIvAOQ1lXAaehjJf4BReLKBuNaFSv/gCB3JBQxxvU5qmp6MsC9HTUr6ylAcsFif3UD3DkZ2wbk8zURUOmYanpRyLwEtaWnAGHFhEkBksM4c6fQKU9LTwQvT0tMhC9PS0THvamuCiG7Pr9Llb0tUSs/AGgSTFpG1M9embSdJWwYXoaavwQvS0VWYcvrUNwYOFFQnVGCCm8emr2MQDr7GDxC/7pjVNsdNUiSXYmpYqLsJOQ/XyMK0PSS/AUNBJQOXKUHIAdiByZPUZfmr6qbIMPN1UmwNnOhcvYETTh6OmnRqLwC39NJwFt/FgGdtn0NNR44XoaanNsrSgBgEKDedAOxuetq36fz7sdu/nWt60FfO1YF1tasm9hm7DJerl1Jt32yqa3IiRot5EOqQoo+itKLx8tEVgRnAMETp0oxRB1nH9KS0ChwhuEcUtu7EPYknRYBD1D6NJRhS+H6EZwX+JsIxA+b3pTngmq8CYrHH6mSx2vpuXyMyxDmsRym6RyRqSexEzWczlRsz8MN2KZRBvmZmS+nZyI+og+o1YFz7slLfd/vXtVPdIeLfB313KV8n/9i+ntxYR3Ya0rbOKp4+vu8P2/bm9dyJAFkhNH/f0v/3h4+X78ylbsfZbWx46tTwgQmmJOT6tfwE739gi' }

gestures = GestureDatabase()
for name, gesture_string in gesture_strings.items():
    gesture = gestures.str_to_gesture(gesture_string)
    gesture.name = name
    gestures.add_gesture(gesture)

class GestureBox(Screen):

    def on_touch_down(self, touch):
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super(GestureBox, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['gesture_path'].append((touch.x, touch.y))
        super(GestureBox, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gestures.find(gesture, minscore=0.09)
            if match:
                # DEBUG: print("{} event".format(match[1].name))

                # we want the ok/cancel button pressed to return so only
                # testing in pic -> settings direction here
                if self.sm.current == 'displayscreen' and match[1].name == 'left_to_right':
                    self.sm.current = 'settingsscreen'
        super(GestureBox, self).on_touch_up(touch)

    def set_screenmanager(self, sm):
        self.sm = sm
