import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--set',choices=['narrow','varied'],required=True);args=p.parse_args()
training=json.loads(Path(args.set+'-train.json').read_text())
test=json.loads(Path(args.set+'-test.json').read_text())
centers={}
for label in sorted({row['label'] for row in training}):
    rows=[row['features'] for row in training if row['label']==label]
    centers[label]=[sum(col)/len(rows) for col in zip(*rows)]
predictions=[]
for row in test:
    distances={label:sum((x-y)**2 for x,y in zip(row['features'],center)) for label,center in centers.items()}
    predictions.append({'id':row['id'],'prediction':min(distances,key=distances.get),'distances':distances})
# Persist every prediction BEFORE loading any held-out answer.
Path(args.set+'-predictions.json').write_text(json.dumps(predictions,indent=2))
answers=json.loads(Path(args.set+'-answers.json').read_text())
correct=sum(row['prediction']==answers[row['id']] for row in predictions)
Path(args.set+'-model.json').write_text(json.dumps(centers,indent=2))
print('test: '+args.set)
print('correct: '+str(correct)+' / '+str(len(test)))
