import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Joy:
    def __init__(self,LATCH, CLOCK,DATA ):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        self.LATCH = LATCH
        self.CLOCK = CLOCK
        self.DATA = DATA

        self.TURBO_BUTTONS = {0: (1,3), 1:(2,4)}
        self.SIMPLE_BUTTONS = {2: "Select", 3: "Start", 4: "Up", 5: "Down", 6: "Left", 7: "Right"}

        self.RELEASE_GAP = 0.25
        self.SETTLE = 0.12

        GPIO.setup(self.LATCH, GPIO.OUT)
        GPIO.setup(self.CLOCK, GPIO.OUT)
        GPIO.setup(self.DATA, GPIO.INPUT, pull_up_down=GPIO.PUD_UP)

        self.fires = {b:self.Fire() for b in self.TURBO_BUTTONS}


    def reading_bits(self):
        GPIO.output(self.LATCH, GPIO.HIGH)
        time.sleep(0.000012)
        GPIO.output(self.LATCH, GPIO.LOW)
        time.sleep(0.000006)

        bits = []

        for _ in range(8):
            bits.append(GPIO.input(self.DATA))
            GPIO.output(self.CLOCK, GPIO.HIGH)
            time.sleep(0.000012)
            GPIO.output(self.CLOCK, GPIO.LOW)
            time.sleep(0.000006)
        return bits

    class Fire:
        def __init__(self):
            self.active = False
            self.turbo = False
            self.last_low = 0.0
            self.prev = 1

    def update(self, bit, v, t):
        f = self.fires[bit]

        if v == 0:
            if not f.active:
                f.active = True
                f.turbo = False
            elif f.prev == 1:
                f.turbo = True
            f.last_low = t
        else:
            if f.active and t - f.last_low > self.RELEASE_GAP:
                f.active = False
                f.turbo = False
        f.prev = v

    def pressed_button(self, bits):
       t = time.time()
       names = []

       for bit, (normal, turbo) in self.TURBO_BUTTONS.items():
           self.update(bit, bits[bit], t)
           f = self.fires[bit]
           if f.active:
               names.append(f"Кнопка: {turbo if f.turbo else normal}")

       for bit, name in self.SIMPLE_BUTTONS.items():
           if bits[bit] == 0:
               names.append(f"Нажата кнопка {name}")
       return tuple(names)

    def run(self):
        shown = ()
        pending = ()
        pending_since = time.time()
        try:
            while True:
                state = self.pressed_button(self.reading_bits())

                if state != pending:
                    pending = state
                    pending_since = time.time()

                if pending != shown and time.time() - pending_since > self.SETTLE:
                    shown = pending
                    if shown:
                        print("\a[НАЖАТО]", ", ".join(shown))
                    else:
                        print("Отпущено")
                time.sleep(0.0005)

        except KeyboardInterrupt:
            GPIO.cleanup()
            print("Тест завершен")
