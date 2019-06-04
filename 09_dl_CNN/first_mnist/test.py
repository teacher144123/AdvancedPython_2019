import torch

def test(model, data, device='cpu'):
    model.eval()

    acc_count = 0
    for i, (image, label) in enumerate(data):
        image = image.to(device)
        label = label.to(device)

        score = model(image)

        pred = torch.argmax(score, dim=1)
        correct = pred.eq(label)
        acc_count += correct.sum().item()

        if i % 100 == 0:
            print('test ({} / {})'.format(i, len(data)))

    acc = acc_count / (len(data) * 16) * 100
    print('----------Acc: {}%----------'.format(acc))
    return acc
