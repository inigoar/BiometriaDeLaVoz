import warnings
import predictor


def main():
    print('Bienvenido a Aplicaciones de la biometría de la voz.')
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    predictor.analyze('Data/S1/spk_000335/trn_017887.wav')


if __name__ == "__main__":
    main()
